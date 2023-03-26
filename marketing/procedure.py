# procedure or function that should be done when a certain order is placed or 
# some event occur in the front end
from marketing.models import Item, Marketing, addresss
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
    
def delete_current_address(id):
    address_instance=addresss.objects.filter(group=id)
    address_instance.delete()
    
    
def delete_current_model(id,flag):
    if flag:
        delete_current_address(id=id)
        delete_current_marketing(id=id)
        item_instance=Item.objects.filter(item_group=id)
        item_instance.delete();
    else:
        delete_current_address(id=id)
        delete_current_marketing(id=id)
        