from django.db import models
from django_jalali.db.models import jDateField, jDateTimeField
from jdatetime import date


class CustomUser(models.Model):
    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    GENDER_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    national_coded = models.CharField(max_length=10)
    birthday_date = jDateField()
    ceremony_datetime = jDateTimeField()
    country = models.CharField(max_length=10, default='Iran')

    def get_first_and_last_name(self):
        first_name, last_name = str(self.full_name).split(' ')
        name = {
            'first_name': first_name,
            'last_name': last_name
        }
        return name

    def get_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year

        if (today.month, today.day) < (self.birthday_date.month, self.birthday_date.day):
            age -= 1

        return age

    def is_birthday(self):
        today = date.today()
        return today.month == self.birthday_date.month and today.day == self.birthday_date.day
