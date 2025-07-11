# Generated by Django 5.1.6 on 2025-03-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0033_alter_dtlt_engineer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtlt',
            name='custom_status',
            field=models.CharField(blank=True, help_text="Enter a custom status if 'Other' is selected.", max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='PGP',
            field=models.CharField(choices=[('Encryption', 'Encryption'), ('Bitlocker', 'Bitlocker'), ('NA', 'NA')], max_length=50),
        ),
        migrations.AlterField(
            model_name='dtlt',
            name='operational_status',
            field=models.CharField(choices=[('Operational', 'Operational'), ('Stock', 'Stock'), ('Other', 'Other')], default='Operational', max_length=100),
        ),
    ]
