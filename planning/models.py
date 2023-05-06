from django.db import models
from django.utils.translation import gettext_lazy as _
from marketing.models import Marketing
from django.utils import timezone
# Create your models here.


class Status(models.Model):
    MARKETING_FINISHED = 1
    PLANNING_IUSSUE = 2
    PLANNING_REJECTION = 3

    STATUS = ((MARKETING_FINISHED, _("THE MARKETING DEPARTMENT APPROVED")),
              (PLANNING_IUSSUE, _("PLANNING DEPARMENT ISSUED A WARNING")),
              (PLANNING_REJECTION, _("PLANNING DEPARMENT HAS REJECTED THE ORDER")))

    work_order_no = models.OneToOneField(
        Marketing,on_delete=models.CASCADE, related_query_name='work_order_no', primary_key=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS, default=MARKETING_FINISHED,)

    class Meta:
        managed = True
        db_table = 'status'


class MaterialList(models.Model):
    matcode = models.CharField(primary_key=True, max_length=6)
    title = models.CharField(max_length=45, blank=True, null=True)
    ref = models.CharField(max_length=36, blank=True, null=True)
    au = models.CharField(max_length=2, blank=True, null=True)
    safstk = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    reorder = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    ar = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    desk = models.CharField(max_length=5, blank=True, null=True)
    ordcst = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True)
    eoq = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    lt = models.DecimalField(
        max_digits=12, decimal_places=1, blank=True, null=True)
    safty = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    auamt = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    spare = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    gr = models.CharField(max_length=4, blank=True, null=True)
    nm = models.CharField(max_length=1, blank=True, null=True)
    pstock = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    ind = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    nsaftystk = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, null=True)
    specno = models.CharField(max_length=10, blank=True, null=True)
    matgroup = models.CharField(max_length=20, blank=True, null=True)
    section = models.CharField(max_length=25, blank=True, null=True)
    group_b = models.CharField(max_length=30, blank=True, null=True)
    group_c = models.CharField(max_length=30, blank=True, null=True)
    group_a = models.CharField(max_length=30, blank=True, null=True)
    abc = models.CharField(max_length=2, blank=True, null=True)
    reordqty = models.DecimalField(
        max_digits=13, decimal_places=3, blank=True, null=True)
    unitrate = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True, null=True)
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
    matcode = models.OneToOneField(
        MaterialList, on_delete=models.CASCADE, primary_key=True)
    qty = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, default=0)
    safe_stock = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True)

    class Meta:
        managed = True
        db_table = 'stock'


class Stock_log(models.Model):
    ADD_OR_CONSUMED = (("ADDED", _("ADDED TO THE STOCK ")),
                       ("CONSUMED", _("TAKEN FROM STOCK")))
    matcode = models.ForeignKey(MaterialList, on_delete=models.CASCADE)
    qty = models.DecimalField(
        max_digits=15, decimal_places=3, blank=True, default=0)
    Add_or_Consumed = models.CharField(max_length=20, choices=ADD_OR_CONSUMED)
    Date = models.DateField(blank=True)
    gnr_no = models.CharField(max_length=40, blank=True, null=True)
    snr_no = models.CharField(max_length=40, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)
    transaction_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'stock_log'


class Po(models.Model):
    srlno = models.BigAutoField(primary_key=True)
    pono = models.CharField(max_length=10, blank=True, null=True)
    prno = models.BigIntegerField(blank=True, null=True)
    poyear = models.CharField(max_length=4, blank=True, null=True)
    matcode = models.CharField(max_length=6, blank=True, null=True)
    ssrl = models.CharField(max_length=2, blank=True, null=True)
    submited = models.BooleanField(default=False)
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
    exdutyin = models.BooleanField(default=False)
    pandfin = models.BooleanField(default=False)
    sltaxin = models.CharField(max_length=12, blank=True, null=True)
    postatus = models.CharField(max_length=10, blank=True, null=True)
    postatusdate = models.DateField(blank=True, null=True)
    gst = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    gstin = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'po'


class Polog(models.Model):
    slno = models.BigAutoField(primary_key=True)
    srlno = models.BigIntegerField(null=True)
    pono = models.CharField(max_length=10)
    prno = models.BigIntegerField()
    matcode = models.CharField(max_length=6)
    ssrl = models.CharField(max_length=2)
    poqty = models.DecimalField(max_digits=17, decimal_places=3)
    poyear = models.CharField(max_length=4)
    podate = models.DateField()
    porate = models.DecimalField(max_digits=17, decimal_places=3)
    vender = models.CharField(max_length=5)
    remark = models.CharField(max_length=50)
    edate = models.DateField()
    enq_ref = models.CharField(max_length=30)
    off_ref = models.CharField(max_length=30)
    mrqdept = models.CharField(max_length=7)
    ex_dut = models.CharField(max_length=10)
    sal_tx = models.CharField(max_length=10)
    pandf = models.CharField(max_length=10)
    fright = models.CharField(max_length=25)
    delivery = models.CharField(max_length=100)
    p_terms = models.CharField(max_length=100)
    rmks = models.CharField(max_length=100)
    ord_acc = models.CharField(max_length=20)
    pri_vari = models.CharField(max_length=100)
    sup_grad = models.CharField(max_length=20)
    pandf1 = models.DecimalField(max_digits=6, decimal_places=3)
    pandfamt = models.DecimalField(max_digits=14, decimal_places=3)
    ex_duty1 = models.DecimalField(max_digits=6, decimal_places=3)
    cst1 = models.DecimalField(max_digits=6, decimal_places=3)
    vat1 = models.DecimalField(max_digits=6, decimal_places=3)
    against = models.CharField(max_length=15)
    deldate = models.DateField()
    srtx1 = models.DecimalField(max_digits=6, decimal_places=3)
    exdutyin = models.BooleanField()
    pandfin = models.BooleanField()
    sltaxin = models.CharField(max_length=12)
    postatus = models.CharField(max_length=10)
    postatusdate = models.DateField()
    logid = models.CharField(max_length=25)
    eddt = models.DateField()
    edtime = models.TimeField()
    gst = models.DecimalField(max_digits=5, decimal_places=2)
    gstin = models.BooleanField()

    class Meta:
        db_table = 'polog'
        managed=True


class Prdetail(models.Model):
    srlno = models.BigAutoField(primary_key=True)
    prno = models.BigIntegerField(blank=True, null=True)
    pono = models.CharField(max_length=10, blank=True, null=True)
    pryear = models.CharField(max_length=4, blank=True, null=True)
    matcode = models.CharField(max_length=6, blank=True, null=True)
    ssrl = models.CharField(max_length=2, blank=True, null=True)
    submited = models.BooleanField(blank=True, null=True)
    pr_qty = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    pr_date = models.DateField(blank=True, null=True)
    rq_date = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=20, blank=True, null=True)
    podate = models.DateField(blank=True, null=True)
    poqty = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    supcode = models.CharField(max_length=20, blank=True, null=True)
    porate = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    lpr = models.CharField(max_length=10, blank=True, null=True)
    lprdt = models.DateField(blank=True, null=True)
    pr_pen = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    stock = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    tpndr = models.CharField(max_length=20, blank=True, null=True)
    apprsr1 = models.CharField(max_length=20, blank=True, null=True)
    apprsr2 = models.CharField(max_length=20, blank=True, null=True)
    apprsr3 = models.CharField(max_length=20, blank=True, null=True)
    apprsr4 = models.CharField(max_length=20, blank=True, null=True)
    apprsr5 = models.CharField(max_length=20, blank=True, null=True)
    apprsr6 = models.CharField(max_length=20, blank=True, null=True)
    apprsr7 = models.CharField(max_length=20, blank=True, null=True)
    apprsr8 = models.CharField(max_length=20, blank=True, null=True)
    apprsr9 = models.CharField(max_length=20, blank=True, null=True)
    apprsr10 = models.CharField(max_length=20, blank=True, null=True)
    pndpo = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    ratehike = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    sugg = models.CharField(max_length=25, blank=True, null=True)
    wor1 = models.CharField(max_length=10, blank=True, null=True)
    wor2 = models.CharField(max_length=10, blank=True, null=True)
    wor3 = models.CharField(max_length=10, blank=True, null=True)
    wor4 = models.CharField(max_length=10, blank=True, null=True)
    wor5 = models.CharField(max_length=10, blank=True, null=True)
    wo5r = models.CharField(max_length=10, blank=True, null=True)
    prremark = models.CharField(max_length=250, blank=True, null=True)
    itremark = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'prdetail'


class Prdetaillog(models.Model):
    slno = models.BigAutoField(primary_key=True)
    srlno = models.IntegerField(blank=True, null=True)
    prno = models.BigIntegerField(blank=True, null=True)
    prno = models.BigIntegerField(blank=True, null=True)
    pono = models.CharField(max_length=10, blank=True, null=True)
    pryear = models.CharField(max_length=4, blank=True, null=True)
    matcode = models.CharField(max_length=6, blank=True, null=True)
    ssrl = models.CharField(max_length=2, blank=True, null=True)
    submited = models.BooleanField(blank=True, null=True)
    pr_qty = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    pr_date = models.DateField(blank=True, null=True)
    rq_date = models.DateField(blank=True, null=True)
    remark = models.CharField(max_length=20, blank=True, null=True)
    podate = models.DateField(blank=True, null=True)
    poqty = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    supcode = models.CharField(max_length=20, blank=True, null=True)
    porate = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    lpr = models.CharField(max_length=10, blank=True, null=True)
    lprdt = models.DateField(blank=True, null=True)
    pr_pen = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    stock = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    tpndr = models.CharField(max_length=20, blank=True, null=True)
    apprsr1 = models.CharField(max_length=20, blank=True, null=True)
    apprsr2 = models.CharField(max_length=20, blank=True, null=True)
    apprsr3 = models.CharField(max_length=20, blank=True, null=True)
    apprsr4 = models.CharField(max_length=20, blank=True, null=True)
    apprsr5 = models.CharField(max_length=20, blank=True, null=True)
    apprsr6 = models.CharField(max_length=20, blank=True, null=True)
    apprsr7 = models.CharField(max_length=20, blank=True, null=True)
    apprsr8 = models.CharField(max_length=20, blank=True, null=True)
    apprsr9 = models.CharField(max_length=20, blank=True, null=True)
    apprsr10 = models.CharField(max_length=20, blank=True, null=True)
    pndpo = models.DecimalField(max_digits=17, decimal_places=3, blank=True, null=True)
    ratehike = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    sugg = models.CharField(max_length=25, blank=True, null=True)
    wor1 = models.CharField(max_length=10, blank=True, null=True)
    wor2 = models.CharField(max_length=10, blank=True, null=True)
    wor3 = models.CharField(max_length=10, blank=True, null=True)
    wor4 = models.CharField(max_length=10, blank=True, null=True)
    wor5 = models.CharField(max_length=10, blank=True, null=True)
    wo5r = models.CharField(max_length=10, blank=True, null=True)
    prremark = models.CharField(max_length=250, blank=True, null=True)
    itremark = models.CharField(max_length=50, blank=True, null=True)
    logid = models.CharField(max_length=25, blank=True, null=True)
    eddt = models.DateField(blank=True, null=True)
    edtime = models.TimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'prdetaillog'
        unique_together = (('slno', 'srlno'),)
