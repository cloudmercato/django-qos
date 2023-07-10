from django_qos import qos


class DummyQosTestCase(qos.QosTestCase):
    def test_func(self):
        pass


class VariousQosTestCase(qos.QosTestCase):
    def test_success(self):
        self.assertTrue(True)

    def test_failed(self):
        self.assertTrue(False)

    def test_error(self):
        raise Exception("An error")
