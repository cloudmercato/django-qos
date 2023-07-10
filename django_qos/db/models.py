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
