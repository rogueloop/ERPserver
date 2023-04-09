from django.forms import ValidationError
from planning.models import Stock_log
from planning.serializer import Stock_log_Serializer

def add_stock_log(verified_data):
    Stock_log_instance=Stock_log_Serializer(data=verified_data)
    try:
        Stock_log_instance.is_valid(raise_exception=True)
        Stock_log_instance.save()
        return Stock_log_instance.data
    except ValidationError as e:
        return {'error': str(e)},