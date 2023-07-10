import unittest
import requests


class QosTestCase(unittest.TestCase):
    pass


class HttpQosTestCase(QosTestCase):
    @property
    def client(self):
        if not hasattr(self, '_client'):
            self._client = requests.Session()
        return self._client

    def assertUrlCode(self, url, code, method='get'):
        func = getattr(self.client, method.lower())
        response = func(url)
        self.assertEqual(response.status_code, code)
        return response

    def assertUrlCode200(self, url, method='get'):
        response = self.assertUrlCode(url, code=200, method=method)
        return response
