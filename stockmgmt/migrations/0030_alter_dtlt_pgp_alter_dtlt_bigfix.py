# Generated by Django 5.1.6 on 2025-03-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0029_rename_av_dtlt_antivirus_rename_dlp_dtlt_dlp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtlt',
            name='PGP',
            field=models.CharField(choices=[('Encryption', 'Encryption'), ('Bitlocker', 'Bitlocker')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='bigfix',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('NA', 'NA')], max_length=50),
        ),
    ]
