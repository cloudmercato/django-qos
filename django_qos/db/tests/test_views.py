from django.test import TestCase
from django.urls import reverse_lazy
from django_qos.db.tests import factories


class TestResultListViewTest(TestCase):
    url = reverse_lazy('testresult-list')

    def test_get_empty(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['object_list'].exists())

    def test_get(self):
        factories.TestResultFactory.create_batch(5)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object_list'].count(), 5)
