# Generated by Django 4.1.7 on 2023-03-24 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("marketing", "0002_alter_marketing_buyer_tel_no_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="addresss",
            name="telephone_no",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name="marketing",
            name="amount",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="billing_status",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="cess",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_checkpost",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_date",
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_dc_date",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_dc_no",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_lr_date",
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_lr_no",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_remarks",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_trns_lr_date",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_trns_lr_no",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_advanced_vehicel_no",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_iniitial_date",
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_iniitial_destination",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_iniitial_exp_time",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_iniitial_packing",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_iniitial_remarks",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="dispatch_iniitial_transporter",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="grand_total",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="mode_of_paymen",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="packing_forwarding_charge",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="prr_dat",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="prr_n",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="prr_remark",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="purpose",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="sub_total",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name="marketing",
            name="tax_gst",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]