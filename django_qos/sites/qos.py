from django.contrib.sites import models
from django_qos import qos


class SiteQosTestCase(qos.HttpQosTestCase):
    """
    Base class for Site QoS.
    """
    proto = 'https'
    domain = None

    def test_get_home(self):
        url = f'{self.proto}://{self.domain}'
        self.assertUrlCode200(url)
