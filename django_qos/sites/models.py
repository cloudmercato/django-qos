from django.db import models


class SiteResult(models.Model):
    result = models.OneToOneField('django_qos.TestResult')
    site = models.ForeignKey('sites.Site')
