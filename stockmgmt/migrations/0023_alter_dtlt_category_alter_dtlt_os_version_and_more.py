# Generated by Django 5.1.6 on 2025-03-04 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0022_alter_dtlt_av_alter_dtlt_bigfix_alter_dtlt_dlp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtlt',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='os_version',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='po_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='sap_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='serial_number',
            field=models.IntegerField(unique=True),
        ),
    ]
