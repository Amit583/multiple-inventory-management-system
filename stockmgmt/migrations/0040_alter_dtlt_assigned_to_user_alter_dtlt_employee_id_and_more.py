# Generated by Django 5.1.6 on 2025-03-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0039_alter_dtlt_asset_age_as_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtlt',
            name='assigned_to_user',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='employee_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='placement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='user_dept',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='user_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
