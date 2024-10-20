import csv

from django.core.management.base import BaseCommand, CommandError

from career.models import Company


class Command(BaseCommand):
    def handle(self, *args, **options):
        companies = Company.objects.all()
        csv_file_name = 'company.csv'

        with open(csv_file_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            for company in companies:
                csv_writer.writerow([company.name, company.email, company.phone])
