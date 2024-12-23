from django.contrib import admin
from .models import InsuranceApplication

@admin.register(InsuranceApplication)
class InsuranceApplicationAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'tax_code', 'registration_address', 'deductible', 'created_at')
    search_fields = ('phone_number', 'tax_code', 'registration_address')
    list_filter = ('deductible', 'created_at')
