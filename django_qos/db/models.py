from django.db import models

STATES = (
    ('success', "Success"),
    ('failure', "Failure"),
    ('error', "Error"),
)


class TestResult(models.Model):
    """
    Stores each probe from QosTestCase.
    """
    timestamp = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=20, choices=STATES)

    name = models.CharField(max_length=300)
    doc = models.TextField(max_length=2000, blank=True, null=True)
    path = models.CharField(max_length=300)

    error = models.TextField(max_length=20000, blank=True, null=True)
    error_msg = models.TextField(max_length=1000, blank=True, null=True)


class RequestResult(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.FloatField()
    # Request
    method = models.CharField(max_length=20)
    host = models.CharField(max_length=100)
    path = models.CharField(max_length=500)
    is_ajax = models.BooleanField()
    # Response
    using = models.CharField(max_length=100, blank=True, null=True)
    queries = models.JSONField(blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    template_name = models.CharField(max_length=500, blank=True, null=True)
    is_rendered = models.BooleanField()
