from unittest import mock
from django.test import TestCase
from django_qos import qos


class HttpQosTestCaseTest(TestCase):
    def test_client(self):
        test_case = qos.HttpQosTestCase()
        self.assertEqual(test_case.client.__class__.__module__, 'requests.sessions')
        self.assertEqual(test_case.client.__class__.__name__, 'Session')

    @mock.patch('requests.Session.get', return_value=mock.MagicMock(status_code=200))
    def test_assert_url_code(self, mock_get):
        test_case = qos.HttpQosTestCase()
        test_case.assertUrlCode(
            url='https://foo.bar',
            code=200,
            method='GET',
        )
        self.assertTrue(mock_get.called)

    @mock.patch('requests.Session.get', return_value=mock.MagicMock(status_code=400))
    def test_assert_url_code_wrong_code(self, mock_get):
        test_case = qos.HttpQosTestCase()
        self.assertRaises(
            AssertionError,
            test_case.assertUrlCode,
            url='https://foo.bar',
            code=200,
            method='GET',
        )
        self.assertTrue(mock_get.called)

    @mock.patch('requests.Session.post', return_value=mock.MagicMock(status_code=200))
    def test_assert_url_code_with_post(self, mock_post):
        test_case = qos.HttpQosTestCase()
        test_case.assertUrlCode(
            url='https://foo.bar',
            code=200,
            method='POST',
        )
        self.assertTrue(mock_post.called)

    @mock.patch('requests.Session.get', return_value=mock.MagicMock(status_code=200))
    def test_assert_url_code_200(self, mock_get):
        test_case = qos.HttpQosTestCase()
        test_case.assertUrlCode200(
            url='https://foo.bar',
            method='GET',
        )
        self.assertTrue(mock_get.called)
