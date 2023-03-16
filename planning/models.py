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