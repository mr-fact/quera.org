import json
from pydoc import describe

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from career.models import Company


class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		while True:
			name = input('Name: ')
			if name == '':
				self.stderr.write('Error: This field cannot be blank.')
			elif len(name) > 50:
				self.stderr.write(f'Error: Ensure this value has at most 50 characters (it has {len(name)}).')
			elif Company.objects.filter(name=name).exists():
				self.stderr.write('Error: That name is already taken.')
			else:
				break
		while True:
			email = input('Email: ')
			try:
				Company(email=email).full_clean()
			except ValidationError as err:
				errors = err.error_dict.get('email', [])
				for error in errors:
					self.stderr.write(f'Error: {error.message}')
				if not errors:
					break
		while True:
			phone = input('Phone: ')
			try:
				Company(phone=phone).full_clean()
			except ValidationError as err:
				errors = err.error_dict.get('phone', [])
				for error in errors:
					self.stderr.write(f'Error: {error.message}')
				if not errors:
					break
		description = input('Description: ')
		if not description:
			description = None

		Company.objects.create(
			name=name,
			email=email,
			phone=phone,
			description=description
		)