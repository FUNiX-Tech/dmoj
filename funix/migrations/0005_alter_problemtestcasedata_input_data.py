# Generated by Django 3.2.21 on 2023-09-16 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funix', '0004_problemtestcasedatatranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemtestcasedata',
            name='input_data',
            field=models.TextField(blank=True, verbose_name='input (criteria)'),
        ),
    ]