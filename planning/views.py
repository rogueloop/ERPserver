

from marketing.procedure import get_status
from rest_framework.decorators import api_view,APIView

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.pagination import PageNumberPagination
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
    queryset = Stock.objects.all()

# updating the current stock
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
    # adding new element to the stock
    
    def post(self,request, *args,**kwargs):
        Serializer=self.get_serializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return JsonResponse({'success':Serializer.data})
    # gives the list of stocks of all material 
    def get(self,request,*args):
        stock_instance=self.queryset.all()
        serializer=Stock_Serializer(stock_instance,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class NotifyLimitAPI(APIView):
    serializer_class = Stock_Serializer
    queryset = Stock.objects.all()
    
    def get(self,request,*args):
        safe_stock=Stock.objects.values_list('safe_stock',flat=True).first()
        stock_instance=Stock.objects.filter(qty__lt=safe_stock)
        serializer=self.serializer_class(stock_instance,many=True)
        less_stock=[]
        for item in serializer.data:
            material_name=MaterialList.objects.get(pk=item['matcode']).title
            item.update({'name':material_name})
            less_stock.append(item)
        return Response({'list':less_stock},status=status.HTTP_200_OK)
    
    

class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
    
class Material_API(generics.GenericAPIView):
    serializer_class =MaterialSerializer 
    pagination_class =MyPagination
    
    queryset = MaterialList.objects.all()
    def post(self,request, *args,**kwargs):
        Serializer=self.get_serializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return JsonResponse({'success':Serializer.data})
    def get(self, request, pk=None):
        
        if pk:
            obj= MaterialList.objects.get(pk=pk)
            serializer =self.get_serializer(obj)
            return Response(serializer.data)
        else:
            page=self.paginate_queryset(self.queryset)
            if page is not None:
                serializer=self.get_serializer(page,many=True)
                return self.get_paginated_response(serializer.data)
            serializer=self.get_serializer(self.queryset,many=True)
            return Response(serializer.data)
