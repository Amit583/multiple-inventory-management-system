# Generated by Django 5.1.6 on 2025-03-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0020_alter_dtlt_av_alter_dtlt_bigfix_alter_dtlt_dlp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtlt',
            name='av',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='bigfix',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='dlp',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='pgp',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=50),
        ),
    ]
