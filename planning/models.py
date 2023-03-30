from django.db import models
from django.utils.translation import gettext_lazy as _
from marketing.models import Marketing
# Create your models here.

class Status(models.Model):
    MARKETING_FINISHED=1
    PLANNING_IUSSUE=2
    PLANNING_REJECTION=3
    
    
    STATUS=((MARKETING_FINISHED,_("THE MARKETING DEPARTMENT APPROVED")),
            (PLANNING_IUSSUE,_("PLANNING DEPARMENT ISSUED A WARNING")),
            (PLANNING_REJECTION,_("PLANNING DEPARMENT HAS REJECTED THE ORDER")))
    
    work_order_no=models.ForeignKey(Marketing,models.DO_NOTHING,related_query_name='work_order_no')
    status=models.PositiveSmallIntegerField(choices=STATUS,default=MARKETING_FINISHED,)
    

    class Meta:
        managed=True
        db_table='Status'
        

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