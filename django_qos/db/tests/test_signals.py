from django.test import TestCase
from django_qos.db import models
from django_qos.db import signals
from django_qos import utils


class PostRunTestRecordTest(TestCase):
    def test_func(self):
        # Setup
        labels = ['django_qos.tests.testproject.testapp.qos']
        suite, result = utils.run_tests(labels)
        # Run
        signals.post_run_tests_record(
            sender=__name__,
            suite=suite,
            result=result
        )
        self.assertTrue(models.TestResult.objects.exists())
