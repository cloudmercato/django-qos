import time
import importlib
import warnings
from django.db import connection
from django_qos import settings
from django_qos.db import models


def get_func(path):
    module_name = path.rsplit('.', 1)[0]
    obj_name = path.rsplit('.', 1)[-1]
    module = importlib.import_module(module_name)
    obj = getattr(module, obj_name)
    return obj


def duration_test(request, response, duration, error):
    return duration > settings.DURATION_THRESHOLD


class RecordMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.func = staticmethod(get_func(settings.RECORD_ENABLE_FUNC))

    def record(self, request, response, duration, error):
        using = getattr(response, 'using', None)
        template_name = getattr(response, 'template_name', None)
        is_rendered = getattr(response, 'is_rendered', False)
        status_code = 0 if response is None else response.status_code
        return models.RequestResult.objects.create(
            duration=duration,
            method=request.method,
            host=request.get_host(),
            path=request.path,
            is_ajax=request.is_ajax(),
            using=using,
            queries=connection.queries,
            status_code=status_code,
            template_name=template_name,
            is_rendered=is_rendered,
        )

    def __call__(self, request):
        t0 = time.time()
        error = None
        try:
            response = self.get_response(request)
        except Exception as err:
            response = None
            error = err
        duration = time.time() - t0
        to_record = self.func(
            request=request,
            response=response,
            duration=duration,
            error=error,
        )
        if to_record:
            try:
                self.record(request, response, duration, error)
            except Exception as err:
                warnings.warn(str(err))
        return response
