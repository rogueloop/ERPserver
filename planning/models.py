from django.db import models
from django.utils.translation import gettext_lazy as _
from marketing.models import Marketing
from django.utils import timezone
# Create your models here.

class Status(models.Model):
    MARKETING_FINISHED=1
    PLANNING_IUSSUE=2
    PLANNING_REJECTION=3
    
    
    STATUS=((MARKETING_FINISHED,_("THE MARKETING DEPARTMENT APPROVED")),
            (PLANNING_IUSSUE,_("PLANNING DEPARMENT ISSUED A WARNING")),
            (PLANNING_REJECTION,_("PLANNING DEPARMENT HAS REJECTED THE ORDER")))
    
    work_order_no=models.OneToOneField(Marketing,models.DO_NOTHING,related_query_name='work_order_no',primary_key=True)
    status=models.PositiveSmallIntegerField(choices=STATUS,default=MARKETING_FINISHED,)
    

    class Meta:
        managed=True
        db_table='status'
        

class MaterialList(models.Model):
    matcode = models.CharField(primary_key=True, max_length=6)
    title = models.CharField(max_length=45, blank=True, null=True)
    ref = models.CharField(max_length=36, blank=True, null=True)
    au = models.CharField(max_length=2, blank=True, null=True)
    safstk = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    reorder = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    ar = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    desk = models.CharField(max_length=5, blank=True, null=True)
    ordcst = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    eoq = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    lt = models.DecimalField(max_digits=12, decimal_places=1, blank=True, null=True)
    safty = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    auamt = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    spare = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    gr = models.CharField(max_length=4, blank=True, null=True)
    nm = models.CharField(max_length=1, blank=True, null=True)
    pstock = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    ind = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    nsaftystk = models.DecimalField(max_digits=15, decimal_places=3, blank=True, null=True)
    specno = models.CharField(max_length=10, blank=True, null=True)
    matgroup = models.CharField(max_length=20, blank=True, null=True)
    section = models.CharField(max_length=25, blank=True, null=True)
    group_b = models.CharField(max_length=30, blank=True, null=True)
    group_c = models.CharField(max_length=30, blank=True, null=True)
    group_a = models.CharField(max_length=30, blank=True, null=True)
    abc = models.CharField(max_length=2, blank=True, null=True)
    reordqty = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    unitrate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    dwgno = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'material_list'
class Bom(models.Model):
    matcode = models.CharField(max_length=8)
    qty = models.DecimalField(max_digits=8, decimal_places=3)
    bpcode = models.CharField(max_length=8)
    bpmatcode = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = True
        db_table = 'bom'

class Product(models.Model):
    productid = models.CharField(primary_key=True, max_length=10)
    ssrl = models.CharField(max_length=2, blank=True, null=True)
    submited = models.BooleanField(blank=True, null=True)
    productname = models.CharField(max_length=50, blank=True, null=True)
    db = models.BooleanField(blank=True, null=True)
    saeid = models.CharField(max_length=5, blank=True, null=True)
    taxid = models.CharField(max_length=5, blank=True, null=True)
    model = models.CharField(max_length=15, blank=True, null=True)
    netwt = models.CharField(max_length=10, blank=True, null=True)
    grosswt = models.CharField(max_length=10, blank=True, null=True)
    partno = models.CharField(max_length=15, blank=True, null=True)
    standard = models.BooleanField(blank=True, null=True)
    bpcode = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product'

class Stock(models.Model):
    matcode=models.OneToOneField(MaterialList,on_delete=models.CASCADE,primary_key=True)
    qty= models.DecimalField(max_digits=15, decimal_places=3, blank=True,default=0)
    safe_stock=models.DecimalField(max_digits=15, decimal_places=3, blank=True)

    class Meta:
        managed = True
        db_table='stock'
        
class Stock_log(models.Model):
    ADD_OR_CONSUMED=(("ADDED",_("ADDED TO THE STOCK ")),
            ("CONSUMED",_("TAKEN FROM STOCK")))
    matcode=models.ForeignKey(MaterialList,on_delete=models.CASCADE)
    qty= models.DecimalField(max_digits=15, decimal_places=3, blank=True,default=0)
    Add_or_Consumed=models.CharField(max_length=20,choices=ADD_OR_CONSUMED)
    Date=models.DateField(blank=True)
    gnr_no=models.CharField(max_length=40,blank=True,null=True)
    snr_no=models.CharField(max_length=40,blank=True,null=True)
    remark=models.CharField(max_length=100,blank=True,null=True)
    transaction_id=models.BigAutoField(primary_key=True)
    class Meta:
        managed = True
        db_table='stock_log'