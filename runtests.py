#!/usr/bin/env python3
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line


def main(argv=None):
    sys.path.append('django_qos/tests/testproject/')
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_qos.tests.testproject.testproject.settings'
    argv = argv or []
    if len(argv) <= 1:
        from django.test.utils import get_runner
        django.setup()
        TestRunner = get_runner(settings)
        test_runner = TestRunner()
        result = test_runner.run_tests([
            "django_qos.tests",
            "django_qos.db.tests",
            "django_qos.sites.tests",
        ])
        return result
    execute_from_command_line(argv)


if __name__ == '__main__':
    sys.exit(bool(main(sys.argv)))
