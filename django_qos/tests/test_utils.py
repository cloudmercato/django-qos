from django.test import TestCase
from django_qos import utils


class RunTestSuite(TestCase):
    def test_func(self):
        labels = ['django_qos.tests.testproject.testapp.qos']
        result = utils.run_tests(labels)
        self.assertTrue(result.testsRun)
