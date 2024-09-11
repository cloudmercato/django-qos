import logging
from django_qos import runners
from django_qos import signals

logger = logging.getLogger('django_qos')


def run_tests(
    test_labels,
    **options
):
    """
    Simple test runner adding pre/post signals.
    """
    runner_class = runners.get_runner_class()
    runner = runner_class(**options)

    signals.pre_run_tests.send(sender=runner, test_labels=test_labels)
    suite, result = runner.run_tests(test_labels)
    signals.post_run_tests.send(sender=runner, suite=suite, result=result)

    return result
