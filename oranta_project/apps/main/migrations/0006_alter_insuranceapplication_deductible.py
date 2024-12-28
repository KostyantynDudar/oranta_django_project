# Generated by Django 5.1.4 on 2024-12-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_uploadedfile_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insuranceapplication',
            name='deductible',
            field=models.CharField(choices=[('23-76', 'Вік: 23-76'), ('30-76', 'Вік: 30-76'), ('no_age', 'Без віку')], max_length=20, verbose_name='Вік'),
        ),
    ]
