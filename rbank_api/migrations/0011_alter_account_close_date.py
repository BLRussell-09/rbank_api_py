# Generated by Django 3.2.8 on 2021-10-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbank_api', '0010_auto_20211023_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='close_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]