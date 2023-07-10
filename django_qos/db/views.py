from django.views.generic.list import ListView
from django_qos.db import models


class TestResultListView(ListView):
    model = models.TestResult
