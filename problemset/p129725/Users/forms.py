import re

from django import forms

from Users.models import CustomUser


class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


    def clean_national_code(self):
        national_code = self.cleaned_data.get('national_code')
        if len(national_code) != 10:
            raise forms.ValidationError("کد ملی باید دقیقاً ۱۰ کاراکتر باشد.")

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        if len(full_name.split()) < 2:
            raise forms.ValidationError("نام کامل باید شامل نام و نام خانوادگی باشد.")

        name_parts = full_name.split()
        for part in name_parts:
            if not re.match(r'^[A-Z][a-z]*$', part):
                raise forms.ValidationError("نام و نام خانوادگی باید با حرف بزرگ شروع شوند و بقیه حروف کوچک باشند.")

        return full_name

