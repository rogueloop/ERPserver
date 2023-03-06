from django.db import models

# Create your models here.



#TODO: setup forigne keys for  addresss Item
#TODO: setup proper values need to be fixed need verification 
#TODO: Create smaller table 
class Marketing(models.Model):
   
    no = models.CharField(max_length=100,primary_key=True)
   
    date = models.DateField()
    customer = models.CharField(max_length=100)
    po_no = models.CharField(max_length=100)
    po_date = models.DateField()
    item = models.CharField(max_length=100)
    consignee_tel_no = models.CharField(max_length=100)
    buyer_tel_no = models.CharField(max_length=100)
    payment_terms = models.CharField(max_length=100)
    paying_authority = models.CharField(max_length=100)
    penalty_clause = models.CharField(max_length=100)
    insurance = models.CharField(max_length=100)
    delivery_date = models.DateField()
    delivery_place = models.CharField(max_length=100)
    freight = models.CharField(max_length=100)
    mode_of_despatch = models.CharField(max_length=100)
    inspection = models.CharField(max_length=100)
    special_instruction = models.CharField(max_length=100)
    despatch_additional_info = models.CharField(max_length=100)
    note = models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    packing_forwarding_charge = models.DecimalField(max_digits=10, decimal_places=2)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    tax_gst = models.DecimalField(max_digits=10, decimal_places=2)
    cess = models.DecimalField(max_digits=10, decimal_places=2)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2)

class addresss(models.Model):
    # no = models.ForeignKey(Marketing, on_delete=models.CASCADE)
    org = models.CharField(max_length=255, blank=True)
    addr_line1 = models.CharField(max_length=255, blank=True)
    addr_line2 = models.CharField(max_length=255, blank=True)
    addr_line3 = models.CharField(max_length=255, blank=True)
    pin = models.CharField(max_length=10, blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    gst_no = models.CharField(max_length=15, blank=True)
    type = models.CharField(max_length=255, blank=True)
# type can be "consignee or buyer"
    class Meta:
        managed = True
        db_table = 'addresss'
class Item(models.Model):
    # no = models.ForeignKey(Marketing,on_delete=models.CASCADE)
    si_no = models.IntegerField(primary_key=True)
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