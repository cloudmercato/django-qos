from unittest import runner
from django_qos import settings
from django.test.runner import DiscoverRunner as BaseDiscoverRunner


class TestResult(runner.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success = []

    def addSuccess(self, test):
        self.success.append(test)
        self._mirrorOutput = True


class TestRunner(runner.TextTestRunner):
    resultclass = TestResult

    def __init__(self, *args, **kwargs):
        self.success = []
        super().__init__(*args, **kwargs)


class DiscoverRunner(BaseDiscoverRunner):
    test_runner = TestRunner

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('interactive', False)
        kwargs.setdefault('keepdb', True)
        super().__init__(*args, **kwargs)

    @classmethod
    def add_arguments(cls, parser):
        parser = super().add_arguments(cls, parser)
        return parser

    def setup_test_environment(self, **kwargs):
        pass

    def teardown_test_environment(self, **kwargs):
        pass

    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass

    def suite_result(self, suite, result, **kwargs):
        return suite, result


def get_runner_class(
    test_runner_class=None,
):
    test_runner_class = test_runner_class or settings.TEST_RUNNER
    test_path = test_runner_class.split('.')
    # Allow for relative paths
    if len(test_path) > 1:
        test_module_name = '.'.join(test_path[:-1])
    else:
        test_module_name = '.'
    test_module = __import__(test_module_name, {}, {}, test_path[-1])
    return getattr(test_module, test_path[-1])
