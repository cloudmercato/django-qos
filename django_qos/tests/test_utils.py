from django.test import TestCase
from django_qos import utils


class GetTestSuite(TestCase):
    def test_func(self):
        suite = utils.get_test_suite(['django_qos.tests.testproject.testapp.qos'])
        self.assertTrue(suite._tests)


class RunTestSuite(TestCase):
    def test_func(self):
        suite = utils.get_test_suite(['django_qos.tests.testproject.testapp.qos'])
        result = utils.run_tests(suite)
        self.assertTrue(result.testsRun)
