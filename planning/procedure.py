import io
from django.forms import ValidationError
from planning.models import Stock_log
from planning.serializer import Stock_log_Serializer   
import openpyxl
from openpyxl.utils import get_column_letter
from io import BytesIO
from django.http import FileResponse, HttpResponse



def add_stock_log(verified_data):
    Stock_log_instance=Stock_log_Serializer(data=verified_data)
    try:
        Stock_log_instance.is_valid(raise_exception=True)
        Stock_log_instance.save()
        return Stock_log_instance.data
    except ValidationError as e:
        return {'error': str(e)},


def get_excel(data,name):
    wb = openpyxl.Workbook()
    ws = wb.active
    
    # add header row
    headers = list(data[0].keys())
    for col_num, header in enumerate(headers, 1):
        col_letter = get_column_letter(col_num)
        ws['{}1'.format(col_letter)] = header
    
    # add data rows
    for row_num, row_data in enumerate(data, 2):
        for col_num, cell_value in enumerate(row_data.values(), 1):
            col_letter = get_column_letter(col_num)
            ws.cell(row=row_num, column=col_num, value=cell_value)

    # modify the filename here
    filename =  name+'.xlsx'
    content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    
    # write the file to a buffer
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    
    # create the HttpResponse object with the file and appropriate headers
    response = HttpResponse(output.read(), content_type=content_type)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response