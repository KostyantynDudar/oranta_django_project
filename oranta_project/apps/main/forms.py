from django import forms
from django.core.exceptions import ValidationError
from .models import InsuranceApplication
import re

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return single_file_clean(data, initial)

def validate_phone_number(value):
    if not re.match(r"^\+380\d{9}$", value):
        raise ValidationError("Номер телефона должен быть в формате +380XXXXXXXXX.")

class InsuranceApplicationForm(forms.ModelForm):
    tech_passports = MultipleFileField(label='Техпаспорта', required=False)
    personal_docs = MultipleFileField(label='Личные документы', required=False)
    phone_number = forms.CharField(
        label="Телефон",
        max_length=13,
        validators=[validate_phone_number],
        help_text="Введите номер в формате +380XXXXXXXXX."
    )

    class Meta:
        model = InsuranceApplication
        fields = ['phone_number', 'tax_code', 'registration_address', 'deductible']
