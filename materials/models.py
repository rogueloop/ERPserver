from django.db import models

# Create your models here.


class Po(models.Model):
    srlno = models.BigAutoField(primary_key=True)
    pono = models.CharField(max_length=10, blank=True, null=True)
    prno = models.BigIntegerField(blank=True, null=True)
    poyear = models.CharField(max_length=4, blank=True, null=True)
    matcode = models.CharField(max_length=6, blank=True, null=True)
    ssrl = models.CharField(max_length=2, blank=True, null=True)
    submited = models.BooleanField(blank=True, null=True)
    poqty = models.DecimalField(
        max_digits=17, decimal_places=3, blank=True, null=True)
    podate = models.DateField(blank=True, null=True)
    porate = models.DecimalField(
        max_digits=17, decimal_places=3, blank=True, null=True)
    vender = models.CharField(max_length=5, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    edate = models.DateField(blank=True, null=True)
    enq_ref = models.CharField(max_length=30, blank=True, null=True)
    off_ref = models.CharField(max_length=30, blank=True, null=True)
    mrqdept = models.CharField(max_length=7, blank=True, null=True)
    ex_dut = models.CharField(max_length=10, blank=True, null=True)
    sal_tx = models.CharField(max_length=10, blank=True, null=True)
    pandf = models.CharField(max_length=10, blank=True, null=True)
    fright = models.CharField(max_length=25, blank=True, null=True)
    delivery = models.CharField(max_length=100, blank=True, null=True)
    p_terms = models.CharField(max_length=100, blank=True, null=True)
    rmks = models.CharField(max_length=100, blank=True, null=True)
    ord_acc = models.CharField(max_length=20, blank=True, null=True)
    pri_vari = models.CharField(max_length=100, blank=True, null=True)
    sup_grad = models.CharField(max_length=20, blank=True, null=True)
    pandf1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    pandfamt = models.DecimalField(
        max_digits=14, decimal_places=3, blank=True, null=True)
    ex_duty1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    cst1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    vat1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    against = models.CharField(max_length=15, blank=True, null=True)
    deldate = models.DateField(blank=True, null=True)
    srtx1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    exdutyin = models.BooleanField(blank=True, null=True)
    pandfin = models.BooleanField(blank=True, null=True)
    sltaxin = models.CharField(max_length=12, blank=True, null=True)
    postatus = models.CharField(max_length=10, blank=True, null=True)
    postatusdate = models.DateField(blank=True, null=True)
    gst = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    gstin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'po'


class Polog(models.Model):
    slno = models.BigAutoField(primary_key=True)
    srlno = models.BigIntegerField(blank=True, null=True)
    pono = models.CharField(max_length=10, blank=True, null=True)
    prno = models.BigIntegerField(blank=True, null=True)
    matcode = models.CharField(max_length=6, blank=True, null=True)
    ssrl = models.CharField(max_length=2, blank=True, null=True)
    poqty = models.DecimalField(
        max_digits=17, decimal_places=3, blank=True, null=True)
    poyear = models.CharField(max_length=4, blank=True, null=True)
    podate = models.DateField(blank=True, null=True)
    porate = models.DecimalField(
        max_digits=17, decimal_places=3, blank=True, null=True)
    vender = models.CharField(max_length=5, blank=True, null=True)
    remark = models.CharField(max_length=50, blank=True, null=True)
    edate = models.DateField(blank=True, null=True)
    enq_ref = models.CharField(max_length=30, blank=True, null=True)
    off_ref = models.CharField(max_length=30, blank=True, null=True)
    mrqdept = models.CharField(max_length=7, blank=True, null=True)
    ex_dut = models.CharField(max_length=10, blank=True, null=True)
    sal_tx = models.CharField(max_length=10, blank=True, null=True)
    pandf = models.CharField(max_length=10, blank=True, null=True)
    fright = models.CharField(max_length=25, blank=True, null=True)
    delivery = models.CharField(max_length=100, blank=True, null=True)
    p_terms = models.CharField(max_length=100, blank=True, null=True)
    rmks = models.CharField(max_length=100, blank=True, null=True)
    ord_acc = models.CharField(max_length=20, blank=True, null=True)
    pri_vari = models.CharField(max_length=100, blank=True, null=True)
    sup_grad = models.CharField(max_length=20, blank=True, null=True)
    pandf1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    pandfamt = models.DecimalField(
        max_digits=14, decimal_places=3, blank=True, null=True)
    ex_duty1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    cst1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    vat1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    against = models.CharField(max_length=15, blank=True, null=True)
    deldate = models.DateField(blank=True, null=True)
    srtx1 = models.DecimalField(
        max_digits=6, decimal_places=3, blank=True, null=True)
    exdutyin = models.BooleanField(blank=True, null=True)
    pandfin = models.BooleanField(blank=True, null=True)
    sltaxin = models.CharField(max_length=12, blank=True, null=True)
    postatus = models.CharField(max_length=10, blank=True, null=True)
    postatusdate = models.DateField(blank=True, null=True)
    logid = models.CharField(max_length=25, blank=True, null=True)
    eddt = models.DateField(blank=True, null=True)
    edtime = models.TimeField(blank=True, null=True)
    gst = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    gstin = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'polog'
