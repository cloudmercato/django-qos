from django.test import TestCase
from django_qos.db import models
from django_qos.db import signals
from django_qos import utils


class PostRunTestRecordTest(TestCase):
    def test_func(self):
        # Setup
        suite = utils.get_test_suite(['django_qos.tests.testproject.testapp.qos'])
        result = utils.run_tests(suite)
        # Run
        signals.post_run_tests_record(
            sender=__name__,
            suite=suite,
            result=result
        )
        self.assertTrue(models.TestResult.objects.exists())
