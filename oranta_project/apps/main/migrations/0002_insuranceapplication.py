# Generated by Django 5.1.4 on 2024-12-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('tax_code', models.CharField(max_length=10, verbose_name='Налоговый код')),
                ('tech_passport', models.FileField(upload_to='tech_passports/', verbose_name='Техпаспорт')),
                ('personal_docs', models.FileField(upload_to='personal_docs/', verbose_name='Личные документы')),
                ('registration_address', models.TextField(verbose_name='Адрес регистрации')),
                ('deductible', models.CharField(choices=[('0', '0 грн'), ('1500', '1500 грн'), ('2500', '2500 грн')], max_length=10, verbose_name='Франшиза')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи заявки')),
            ],
        ),
    ]
