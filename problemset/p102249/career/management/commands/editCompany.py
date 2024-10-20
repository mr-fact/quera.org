from textwrap import dedent

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError

from career.models import Company


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('company_name')
        parser.add_argument('--name')
        parser.add_argument('--email')
        parser.add_argument('--phone')
        parser.add_argument('--description')

    def handle(self, *args, **options):
        try:
            company = Company.objects.get(name=options['company_name'])
        except Company.DoesNotExist as err:
            raise CommandError(err)
        name = options.get('name')
        email = options.get('email')
        phone = options.get('phone')
        description = options.get('description')
        if name is not None:
            company.name = name
        if email is not None:
            company.email = email
        if phone is not None:
            company.phone = phone
        if description:
            company.description = description


        if Company.objects.filter(name=name).exists():
            raise CommandError('Error: That name is already taken.')
        try:
            company.full_clean()
        except ValidationError as err:
            for field_name, errors in err.error_dict.items():
                for error in errors:
                    # print(error.messages[0])
                    if error.message == 'This field cannot be blank.':
                        raise CommandError(f'{field_name.capitalize()} cannot be blank.')
                    else:
                        raise CommandError(f'Error: {error.messages[0]}')

        company.save()
            # errors = err.error_dict
            # print(errors)
        # if len(name) > 50:
        #     raise CommandError(f'Error: Ensure this value has at most 50 characters (it has {len(name)}).')
        #
        # company.phone = phone
        # company.email = email
        # company.name = name
        # company.description = description