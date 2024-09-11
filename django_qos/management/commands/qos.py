import sys
import argparse
from django.core.management.commands.test import Command as TestCommand
from django_qos import utils


class Command(TestCommand):
    help = """Run QoS tests"""

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser._option_string_actions['--keepdb'].default = True
        parser._option_string_actions['--keepdb'].help = argparse.SUPPRESS
        parser._option_string_actions['--pattern'].default = 'qos.py'
        return parser

    def handle(self, *test_labels, **options):
        results = utils.run_tests(test_labels, **options)
        if results:
            sys.exit(1)
