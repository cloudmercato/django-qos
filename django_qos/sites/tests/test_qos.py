from unittest import mock
from django.test import TestCase
from django_qos.sites import qos


class SiteQosTestCaseTest(TestCase):
    @mock.patch('requests.Session.get', return_value=mock.MagicMock(status_code=200))
    def test_get_home(self, mock_get):
        test_case = qos.SiteQosTestCase()
        test_case.test_get_home()
        self.assertTrue(mock_get.called)
        url = f'{test_case.proto}://{test_case.domain}'
        self.assertEqual(mock_get.call_args[0][0], url)
