# Generated by Django 3.2.8 on 2021-10-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbank_api', '0003_account_joint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='open_date',
            field=models.DateField(blank=True),
        ),
    ]
