from datetime import date
from django.core.management.base import BaseCommand, CommandError
from django_qos.db import models


class Command(BaseCommand):
    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument('--date', required=False, type=date.fromisoformat)
        parser.add_argument('--all', action="store_true")

    def handle(self, **options):
        qos_date = options['date'] or date.today()
        qs = models.TestResult.objects.all()
        if not options['all']:
            qs = qs.filter(timestamp__date=qos_date)
        count, _ = qs.delete()
        print("Delete %d" % count)
