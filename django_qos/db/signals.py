from django.dispatch import Signal
from django_qos.db import models


pre_record = Signal()
post_record = Signal()


def post_run_tests_record(sender, suite, result, **kwargs):
    """
    This function must be registered as a `django_qos.signals.post_run_tests` signal.
    It emits `pre_record` and `post_record` for each new `TestResult`.
    """
    for test in result.success:
        state = 'success'
        pre_record.send(sender, suite=suite, result=result, test=test)
        test_result = models.TestResult.objects.create(
            state=state,
            name=test._testMethodName,
            doc=test._testMethodDoc,
            path=test.id(),
        )
        post_record.send(sender, suite=suite, result=result, test=test, test_result=test_result)

    def make_err(test, traceback, state):
        pre_record.send(sender, suite=suite, result=result, test=test)
        models.TestResult.objects.create(
            state=state,
            name=test._testMethodName,
            doc=test._testMethodDoc,
            path=test.id(),
            error=traceback,
            error_msg=traceback.splitlines()[-1].split(':')[-1].strip(),
        )
        post_record.send(
            sender,
            suite=suite,
            result=result,
            test=test,
            test_result=traceback
        )
    for test, traceback in result.failures:
        make_err(test, traceback, 'failure')
    for test, traceback in result.errors:
        make_err(test, traceback, 'error')
