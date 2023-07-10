import factory


class TestResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'django_qos_db.TestResult'
