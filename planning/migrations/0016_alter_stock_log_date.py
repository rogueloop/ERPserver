# Generated by Django 4.1.7 on 2023-04-09 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0015_alter_stock_log_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_log',
            name='Date',
            field=models.DateField(blank=True),
        ),
    ]