from django.core.management.base import BaseCommand
from django_qos import utils


class Command(BaseCommand):
    help = """Run QoS tests"""

    def add_arguments(self, parser):
        parser.add_argument(
            'args', metavar='module_paths', nargs='*',
            help='Path to TestCases to launch.'
        )

    def print_pre_test(self, suite):
        self.stdout.write("Tests:")
        for subsuite in suite._tests:
            self.stdout.write(f"- {subsuite.__class__.__module__}.{subsuite.__class__.__name__}:")
            for test_case in subsuite._tests:
                self.stdout.write(f"  - {test_case}:")

    def print_post_test(self, suite, results):
        self.stdout.write(f"{results}")

    def handle(self, *module_paths, **options):
        suite = utils.get_test_suite(module_paths)
        if options['verbosity'] > 0:
            self.print_pre_test(suite)

        test_options = {
            'verbosity': options['verbosity'],
        }
        results = utils.run_tests(suite, **test_options)

        if options['verbosity'] > 0:
            self.print_post_test(suite, results)
