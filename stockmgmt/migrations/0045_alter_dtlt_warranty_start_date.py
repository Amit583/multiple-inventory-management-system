# Generated by Django 5.1.6 on 2025-03-11 10:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0044_alter_dtlt_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtlt',
            name='warranty_start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
