import logging
import unittest
import importlib
import io
from django_qos import settings
from django_qos import signals

logger = logging.getLogger('django_qos')


class TestResult(unittest.runner.result.TestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.success = []

    def addSuccess(self, test):
        self.success.append(test)
        self._mirrorOutput = True


class TestRunner(unittest.TextTestRunner):
    resultclass = TestResult

    def __init__(self, stream=None, *args, **kwargs):
        if stream is None:
            stream = io.StringIO()
        super().__init__(stream=stream, *args, **kwargs)


def get_test_suite(module_paths):
    """
    Create a test suite from apps' paths or `settings.QOS_APPS` if
    is `module_paths` is empty.
    """
    is_module = True
    suite = unittest.TestSuite()
    if not module_paths:
        module_paths = ['%s.qos' % app for app in settings.APPS]
    for app in module_paths:
        try:
            module_and_class = app.split('.')
            if len(module_and_class) == 3:
                module_name = '.'.join(module_and_class[:2])
                module = importlib.import_module(module_name)
                if not hasattr(module, module_and_class[2]):
                    logger.debug('No QoS in %s', app)
                    continue
                module = getattr(module, module_and_class[2])
                is_module = False
            else:
                module = importlib.import_module(app)
        except ImportError:
            logger.warning('Cannot import %s', app)
            continue
        if is_module:
            sub_suite = unittest.TestLoader().loadTestsFromModule(module)
        else:
            sub_suite = unittest.TestLoader().loadTestsFromTestCase(module)
        suite._tests.extend(sub_suite._tests)
    return suite


def run_tests(
    suite,
    verbosity=0,
):
    """
    Simple test runner adding pre/post signals.
    """
    runner = TestRunner(
        verbosity=verbosity,
    )
    signals.pre_run_tests.send(sender=runner, suite=suite)
    result = runner.run(suite)
    signals.post_run_tests.send(sender=runner, suite=suite, result=result)
    return result
