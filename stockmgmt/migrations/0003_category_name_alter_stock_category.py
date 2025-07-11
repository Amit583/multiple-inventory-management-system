# Generated by Django 5.1.6 on 2025-02-20 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmt', '0002_category_alter_stock_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, choices=[('Furniture', 'Furniture'), ('It equipment', 'It equipment'), ('phone', 'phone')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stockmgmt.category'),
        ),
    ]
