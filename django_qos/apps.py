from django.apps import AppConfig
from django_qos import signals


class DjangoQosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_qos'
    verbose_name = 'QoS'

    def ready(self):
        signals.post_run_tests.connect(signals.post_run_tests_email)
