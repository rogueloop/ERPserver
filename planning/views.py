

from datetime import timezone
from marketing.procedure import get_status
from rest_framework.decorators import api_view
import psycopg2
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status,generics

from planning.procedure import add_stock_log

from .serializer import BomSerializer, MaterialSerializer, Product_Serializer, Stock_Serializer, Stock_log_Serializer
from .models import Bom, MaterialList, Product, Stock
# Create your views here.
@api_view(['get'])
def list_bom(request):
    list_=Bom.objects.all();
    B=BomSerializer(list_,many=True).data
    bom_list=[]
    result=dict()
    for each in B:
        
        bom_list.append(each)
    result.update({'Bom':bom_list})
        
        
    return JsonResponse(result,safe=False)

@api_view(['get'])
def list_product(request):
    list_=Product.objects.all();
    B=Product_Serializer(list_,many=True).data
    
    return JsonResponse(B,safe=False)

@api_view(['get'])
def list_materials(request):
    list_=MaterialList.objects.all();
    B=MaterialSerializer(list_,many=True).data
    
    return JsonResponse(B,safe=False)



@api_view(['GET'])
def get_bom(request,pk):
    try:
        product=Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse("The product does not exist",status=status.HTTP_400_BAD_REQUEST)
    serialzer=Product_Serializer(product,many=False).data
    bom=BomSerializer(Bom.objects.filter(bpcode__exact=str(serialzer['bpcode'])),many=True).data
    items=[]
    for each_item in bom:
        each=dict(each_item)
        material=MaterialSerializer(MaterialList.objects.get(pk=each_item['matcode']),many=False).data
        each_item.update({'title':material['title']})
        items.append(each_item)
    result={serialzer['productname']:items}
    return JsonResponse(result,safe=False)





@api_view(['GET'])
def get_stat(request,pk):
    a=get_status(pk=pk)
    
    return Response(a)

class AddStockAPI(generics.GenericAPIView):
    serializer_class = Stock_Serializer

    def put(self, request, *args, **kwargs):
        data = request.data
        matcode = data.get('matcode')
        qty = data.get('qty')
        
        if not matcode or not qty:
            return Response({'Error': 'Missing required field(s)'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            stock_instance = Stock.objects.get(pk=matcode)
            stock_instance.qty+= int(qty)
            stock_instance.save()
            # assuming add_stock_log is a function that logs the stock addition
            log=add_stock_log({'matcode': matcode, 'qty': qty, 'Add_or_Consumed':"ADDED",
                           'Date':data.get('Date'),'gnr_no':data.get('gnr_no'),'snr_no':data.get('snr_no'),'remark':data.get('remark')})
            return Response({'Success': 'Stock added successfully','log':log},
                            status=status.HTTP_200_OK)

        except Stock.DoesNotExist:
            return Response({'Error': 'Stock does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)
    def post(self,request, *args,**kwargs):
        Serializer=self.get_serializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return JsonResponse({'success':Serializer.data})