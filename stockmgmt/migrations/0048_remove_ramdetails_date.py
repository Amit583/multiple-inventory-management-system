# Generated by Django 5.1.6 on 2025-03-17 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0047_ramdetails_date_ramdetails_invoiceno_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ramdetails',
            name='date',
        ),
    ]
