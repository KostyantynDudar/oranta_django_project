from django import forms
from .models import InsuranceApplication

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

class InsuranceApplicationForm(forms.ModelForm):
    tech_passports = MultipleFileField(label='Техпаспорта', required=False)
    personal_docs = MultipleFileField(label='Личные документы', required=False)

    class Meta:
        model = InsuranceApplication
        fields = ['phone_number', 'tax_code', 'registration_address', 'deductible']
