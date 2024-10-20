from cgi import parse

from django.core.management.base import BaseCommand, CommandError
from career.models import Company


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('companies', nargs='*')
        parser.add_argument('--all', action='store_true')

    def handle(self, *args, **options):
        if options.get('all'):
            Company.objects.all().delete()
        else:
            errors = []
            for name in options.get('companies'):
                try:
                    company = Company.objects.get(name=name)
                    company.delete()
                except Company.DoesNotExist as err:
                    errors.append(f'{name} matching query does not exist.')

            self.stderr.write('\n'.join(errors))
