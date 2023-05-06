from django.conf import settings
from django.db import models
import datetime

# Create your models here.
#TODO: setup forigne keys for  addresss Item
#TODO: setup proper values need to be fixed need verification 
#TODO: Create smaller table 
class Marketing(models.Model):
    no = models.CharField(max_length=100,primary_key=True)
    date = models.DateField(blank=True,null=True)
    customer = models.CharField(max_length=100,null=True)
    po_no = models.CharField(max_length=100,blank=True,null=True)
    po_date = models.DateField(blank=True,null=True)
    marketing_item = models.CharField(max_length=100,null=True)
    consignee_tel_no = models.CharField(max_length=100,blank=True,null=True)
    buyer_tel_no = models.CharField(max_length=100,blank=True,null=True)
    payment_terms = models.CharField(max_length=100,blank=True,null=True)
    paying_authority = models.CharField(max_length=100,blank=True,null=True)
    penalty_clause = models.CharField(max_length=100,blank=True,null=True)
    insurance = models.CharField(max_length=100,blank=True,null=True)
    delivery_date = models.DateField(blank=True,null=True)
    delivery_place = models.CharField(max_length=100,blank=True,null=True)
    freight = models.CharField(max_length=100,blank=True,null=True)
    mode_of_despatch = models.CharField(max_length=100,blank=True,null=True)
    inspection = models.CharField(max_length=100,blank=True,null=True)
    special_instruction = models.CharField(max_length=100,blank=True,null=True)
    despatch_additional_info = models.CharField(max_length=100,blank=True,null=True)
    note = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.CharField(max_length=100,blank=True,null=True)
    prr_no= models.CharField(max_length=100,blank=True,null=True)
    prr_date = models.CharField(max_length=100,blank=True,null=True)
    amount =models.CharField(max_length=100,blank=True,null=True)
    mode_of_payment =models.CharField(max_length=100,blank=True,null=True)
    purpose =models.CharField(max_length=100,blank=True,null=True)
    prr_remark =models.CharField(max_length=100,blank=True,null=True)
    billing_status = models.CharField(max_length=100,blank=True,null=True)

    dispatch_iniitial_date= models.DateField(blank=True,null=True)
    dispatch_iniitial_remarks=models.CharField(max_length=100,blank=True,null=True)
    dispatch_iniitial_destination=models.CharField(max_length=100,blank=True,null=True)
    dispatch_iniitial_transporter=models.CharField(max_length=100,blank=True,null=True)
    dispatch_iniitial_packing=models.CharField(max_length=100,blank=True,null=True)
    dispatch_iniitial_exp_time=models.CharField(max_length=100,blank=True,null=True)

    dispatch_advanced_date=models.DateField(blank=True,null=True)
    dispatch_advanced_checkpost=models.CharField(max_length=100,blank=True,null=True)
    dispatch_advanced_trns_lr_no=models.CharField(max_length=100,blank=True,null=True)
    dispatch_advanced_trns_lr_date=models.CharField(max_length=100,blank=True,null=True)
    dispatch_advanced_dc_no=models.CharField(max_length=100,blank=True,null=True)
    dispatch_advanced_dc_date=models.CharField(max_length=100,blank=True,null=True)
    dispatch_advanced_lr_no=models.CharField(max_length=100,blank=True,null=True)
    dispatch_advanced_lr_date=models.DateField(blank=True,null=True)
    dispatch_advanced_vehicel_no=models.CharField(max_length=100,blank=True,null=True)
    dispatch_advanced_remarks=models.CharField(max_length=100,blank=True,null=True)

    packing_forwarding_charge =models.CharField(max_length=100,blank=True,null=True)
    freight =models.CharField(max_length=100,blank=True,null=True)
    sub_total =models.CharField(max_length=100,blank=True,null=True)
    tax_gst =models.CharField(max_length=100,blank=True,null=True)
    cess =models.CharField(max_length=100,blank=True,null=True)
    grand_total =models.CharField(max_length=100,blank=True,null=True)
        
    def __str__(self):
            return self.no
    class Meta:
        managed = True
        db_table = "marketing"

class addresss(models.Model):
    # no = models.ForeignKey(Marketing on_delete=models.CASCADE)
    group = models.ForeignKey("Marketing", on_delete=models.CASCADE,default=None,related_query_name='group' )
    org = models.CharField(max_length=255, blank=True,null=True)
    address_line_1 = models.CharField(max_length=255, blank=True,null=True)
    address_line_2 = models.CharField(max_length=255, blank=True,null=True)
    address_line_3 = models.CharField(max_length=255, blank=True,null=True)
    pin = models.CharField(max_length=10, blank=True,null=True)
    phone_no = models.CharField(max_length=15, blank=True,null=True)
    gst_no = models.CharField(max_length=15, blank=True,null=True)
    type = models.CharField(max_length=255, blank=True,null=True)
    telephone_no= models.CharField(max_length=15, blank=True,null=True)
    
    def __str__(self):
        return self.group
# type can be "consignee or buyer"
    class Meta:
        managed = True
        db_table = 'addresss'
class Item(models.Model):
    # no = models.ForeignKey(Marketing,on_delete=models.CASCADE)
    item_group = models.ForeignKey("Marketing", on_delete=models.CASCADE,default=None,related_query_name='item_group')
    si_no = models.IntegerField(primary_key=False,blank=True,null=True)
    is_std = models.BooleanField(blank=True,null=True)
    item = models.CharField(max_length=100,blank=True,null=True)
    rating = models.CharField(max_length=100,blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    unit = models.CharField(max_length=100,blank=True,null=True)
    model = models.CharField(max_length=100,blank=True,null=True)
    wo_nos = models.CharField(max_length=100,blank=True,null=True)
    basic_rate = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0,null=True)
    basic_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0,null=True)
    dp = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0,null=True)
    net_weight_per_unit = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0,null=True)
    gross_weight_per_unit = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0,null=True)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2,blank=True,default=0,null=True)
    serial_nos = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.item_group
    class Meta:
        managed = True
        db_table = "item"