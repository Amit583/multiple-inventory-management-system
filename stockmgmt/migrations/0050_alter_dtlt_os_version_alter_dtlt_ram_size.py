# Generated by Django 5.1.6 on 2025-03-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0049_alter_dtlt_encryption_alter_dtlt_device_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtlt',
            name='os_version',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='ram_size',
            field=models.PositiveIntegerField(help_text='Size in GB'),
        ),
    ]
