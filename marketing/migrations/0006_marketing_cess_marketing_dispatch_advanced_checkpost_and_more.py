# Generated by Django 4.1.7 on 2023-03-25 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0005_remove_marketing_cess_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketing',
            name='cess',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_checkpost',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_dc_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_dc_no',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_lr_date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_lr_no',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_remarks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_trns_lr_date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_trns_lr_no',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='dispatch_advanced_vehicel_no',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='grand_total',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='packing_forwarding_charge',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='sub_total',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='marketing',
            name='tax_gst',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
