from Users.models import CustomUser
from django.contrib import admin

from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'gender', 'national_code', 'birthday_date')
    search_fields = ('username', 'full_name')
    ordering = ('ceremony_datetime', )

    def first_name(self, user):
        if user.full_name:
            return user.get_first_and_last_name()['first_name']
        else:
            return ''

    def last_name(self, user):
        if user.full_name:
            return user.get_first_and_last_name()['last_name']
        else:
            return ''
