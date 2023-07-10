from django.apps import AppConfig
from django_qos.db import signals as db_signals
from django_qos.sites import signals as sites_signals


class SitesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sites'
    verbose_name = 'QoS Sites'
    label = 'django_qos_sites'

    def ready(self):
        db_signals.post_record.connect(sites_signals.post_record_site)
