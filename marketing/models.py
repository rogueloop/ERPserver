from django.db import models
import datetime

# Create your models here.
#TODO: setup forigne keys for  addresss Item
#TODO: setup proper values need to be fixed need verification 
#TODO: Create smaller table 
class Marketing(models.Model):
    no = models.CharField(max_length=100,primary_key=True)
    date = models.DateField()
    customer = models.CharField(max_length=100)
    po_no = models.CharField(max_length=100,blank=True)
    po_date = models.DateField()
    marketing_item = models.CharField(max_length=100)
    consignee_tel_no = models.CharField(max_length=100,blank=True)
    buyer_tel_no = models.CharField(max_length=100,blank=True)
    payment_terms = models.CharField(max_length=100,blank=True)
    paying_authority = models.CharField(max_length=100,blank=True)
    penalty_clause = models.CharField(max_length=100,blank=True)
    insurance = models.CharField(max_length=100,blank=True)
    delivery_date = models.DateField(blank=True)
    delivery_place = models.CharField(max_length=100,blank=True)
    freight = models.CharField(max_length=100,blank=True)
    mode_of_despatch = models.CharField(max_length=100,blank=True)
    inspection = models.CharField(max_length=100,blank=True)
    special_instruction = models.CharField(max_length=100,blank=True)
    despatch_additional_info = models.CharField(max_length=100,blank=True)
    note = models.CharField(max_length=100,blank=True)
    remarks = models.CharField(max_length=100,blank=True)
    prr_n= models.CharField(max_length=100,blank=True)
    prr_dat = models.CharField(max_length=100,blank=True)
    amount =models.CharField(max_length=100,blank=True)
    mode_of_paymen =models.CharField(max_length=100,blank=True)
    purpose =models.CharField(max_length=100,blank=True)
    prr_remark =models.CharField(max_length=100,blank=True)
    billing_status = models.CharField(max_length=100,blank=True)

    dispatch_iniitial_date= models.DateField(blank=True,default=datetime.date.today)
    dispatch_iniitial_remarks=models.CharField(max_length=100,blank=True)
    dispatch_iniitial_destination=models.CharField(max_length=100,blank=True)
    dispatch_iniitial_transporter=models.CharField(max_length=100,blank=True)
    dispatch_iniitial_packing=models.CharField(max_length=100,blank=True)
    dispatch_iniitial_exp_time=models.CharField(max_length=100,blank=True)

    dispatch_advanced_date=models.DateField(blank=True,default=datetime.date.today)
    dispatch_advanced_checkpost=models.CharField(max_length=100,blank=True)
    dispatch_advanced_trns_lr_no=models.CharField(max_length=100,blank=True)
    dispatch_advanced_trns_lr_date=models.CharField(max_length=100,blank=True)
    dispatch_advanced_dc_no=models.CharField(max_length=100,blank=True)
    dispatch_advanced_dc_date=models.CharField(max_length=100,blank=True)
    dispatch_advanced_lr_no=models.CharField(max_length=100,blank=True)
    dispatch_advanced_lr_date=models.DateField(blank=True,default=datetime.date.today)
    dispatch_advanced_vehicel_no=models.CharField(max_length=100,blank=True)
    dispatch_advanced_remarks=models.CharField(max_length=100,blank=True)

    packing_forwarding_charge =models.CharField(max_length=100,blank=True)
    freight =models.CharField(max_length=100,blank=True)
    sub_total =models.CharField(max_length=100,blank=True)
    tax_gst =models.CharField(max_length=100,blank=True)
    cess =models.CharField(max_length=100,blank=True)
    grand_total =models.CharField(max_length=100,blank=True)
        
    def __str__(self):
            return self.no
    class Meta:
        managed = True
        db_table = "marketing"

class addresss(models.Model):
    # no = models.ForeignKey(Marketing on_delete=models.CASCADE)
    group = models.ForeignKey("Marketing", models.DO_NOTHING,default=None,related_query_name='group' )
    org = models.CharField(max_length=255, blank=True)
    addr_line1 = models.CharField(max_length=255, blank=True)
    addr_line2 = models.CharField(max_length=255, blank=True)
    addr_line3 = models.CharField(max_length=255, blank=True)
    pin = models.CharField(max_length=10, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    gst_no = models.CharField(max_length=15, blank=True)
    type = models.CharField(max_length=255, blank=True)
    telephone_no= models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.group
# type can be "consignee or buyer"
    class Meta:
        managed = True
        db_table = 'addresss'
class Item(models.Model):
    # no = models.ForeignKey(Marketing,on_delete=models.CASCADE)
    item_group = models.ForeignKey("Marketing", models.DO_NOTHING,default=None,related_query_name='item_group')
    si_no = models.IntegerField(primary_key=False)
    is_std = models.BooleanField()
    item = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    wo_nos = models.CharField(max_length=100)
    basic_rate = models.DecimalField(max_digits=10, decimal_places=2)
    basic_amount = models.DecimalField(max_digits=10, decimal_places=2)
    dp = models.DecimalField(max_digits=10, decimal_places=2)
    net_weight_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    gross_weight_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_weight = models.DecimalField(max_digits=10, decimal_places=2)
    serial_nos = models.CharField(max_length=100)

    def __str__(self):
        return self.item_group
    class Meta:
        managed = True
        db_table = "item"