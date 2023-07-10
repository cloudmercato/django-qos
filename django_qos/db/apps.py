from django.apps import AppConfig
from django_qos import signals


class DbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_qos.db'
    verbose_name = 'QoS Database'
    label = 'django_qos_db'

    def ready(self):
        from django_qos.db import signals as db_signals
        signals.post_run_tests.connect(db_signals.post_run_tests_record)
