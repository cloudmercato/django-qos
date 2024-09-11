from unittest import mock
from django.test import TestCase
from django_qos import signals
from django_qos import utils


class PostRunTestEmailTest(TestCase):
    def test_func(self):
        # Setup
        test_labels = ['django_qos.tests.testproject.testapp.qos']
        suite, result = utils.run_tests(test_labels)
        # Run
        signals.post_run_tests_email(
            sender=__name__,
            suite=suite,
            result=result
        )
        self.assertTrue(suite._tests)

    @mock.patch('django_qos.signals.post_run_tests_email')
    def test_auto_connect(self, mock_signal):
        signals.post_run_tests.send(
            'foo',
            suite=mock.Mock(),
            result=mock.Mock(failures=[], errors=[], success=[])
        )
        self.assertFalse(mock_signal.called)
