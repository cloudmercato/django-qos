from django.conf import settings


def get_setting(key, default=None):
    param_key = f"QOS_{key}"
    if not hasattr(settings, param_key):
        return default
    return getattr(settings, param_key)


DEFAULT_APPS = [
    app for app in settings.INSTALLED_APPS
    if not app.startswith('django.')
]
APPS = get_setting('APPS', DEFAULT_APPS)

DEFAULT_SERVER_EMAIL = settings.SERVER_EMAIL
SERVER_EMAIL = get_setting('SERVER_EMAIL', DEFAULT_SERVER_EMAIL)

DEFAULT_MAILS = []
MAILS = get_setting('MAILS', DEFAULT_MAILS)

DEFAULT_TEST_RUNNER = 'django_qos.runners.DiscoverRunner'
TEST_RUNNER = get_setting('TEST_RUNNER', DEFAULT_TEST_RUNNER)
