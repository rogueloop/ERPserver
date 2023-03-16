# procedure or function that should be done when a certain order is placed or 
# some event occur in the front end
from marketing.models import Marketing
from planning.models import Status
from planning.serializer import StatusSerializer



def get_status(pk):
    try:
        status=Status.objects.get(id=pk)
        return status.status
    except Status.DoesNotExist:
        return 0;
    


def add_status(woso):
    obj={'work_order_no':woso}
    status_object=StatusSerializer(data=obj)
    if status_object.is_valid():
        status_object.save
    return status_object.error_messages




def delete_current_marketing(id):
    marketing_instance=Marketing.objects.filter(no=id)
    marketing_instance.delete()