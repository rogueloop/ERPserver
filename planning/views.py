from rest_framework.decorators import api_view, APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from planning.procedure import add_stock_log, get_excel
from .serializer import BomSerializer, MaterialSerializer, Product_Serializer, Stock_Serializer, Stock_log_Serializer,Pr_Serializer
from .models import Bom, MaterialList, Product, Stock,Prdetail
from django.db import transaction
from django.db.models import F

# Create your views here.


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class Product_API_View(APIView):
    serializer_class = Product_Serializer
    queryset = Product.objects.all()

    def get(self, request, pk=None):
        try:
            if pk:
                obj = Product.objects.get(pk=pk)
                serializer = self.serializer_class(obj)
                return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'message': str(Product.DoesNotExist)}, status=status.HTTP_404_NOT_FOUND)
        else:
            paginator = MyPagination()
            page = paginator.paginate_queryset(self.queryset.all(), request)

            if page is not None:

                serializer = self.serializer_class(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            else:
                serializer = self.serializer_class(
                    self.queryset.all(), many=True)
                return Response(serializer.data)

    def post(self, request, *args):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'message': str(Product.DoesNotExist)}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Bom_API_View(APIView):
    serializer_class = BomSerializer

    def get(self, request,*args,**kwargs):
        if 'product_id' in kwargs:
            product_id = kwargs['product_id']
        else:
            product_id = kwargs['pk']
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({'Error_message': "The product does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        serialzer = Product_Serializer(product, many=False).data
        bom = self.serializer_class(Bom.objects.filter(
            bpcode__exact=str(serialzer['bpcode'])), many=True).data
        if len(bom)==0:
            return Response("No bom found",status=status.HTTP_404_NOT_FOUND)
        items = []
        for each_item in bom:
            each = dict(each_item)
            material = MaterialSerializer(MaterialList.objects.get(
                pk=each_item['matcode']), many=False).data
            each_item.update({'title': material['title']})
            items.append(each_item)
        result = {serialzer['productname']: items}
        return Response(result)

    def post(self, request, *args, **kwargs):
        data = request.data
        if (Product.objects.filter(productid=data.get('product_id')).exists()):
            # bill of material (bom)
            bom_data = list(data.get('bom'))
            
            with transaction.atomic():
                for material in bom_data:
                    bom_instance = self.serializer_class(data=material)
                    bom_instance.is_valid(raise_exception=True)
                    bom_instance.save()
            response_data = {'message': 'BOM created successfully'}
            response_data.update(self.get(request,product_id=data.get('product_id')).data)
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response("The product is not registered, register the product before adding bom")

    def put(self, request, *args, **kwargs):
        if 'product_id' in kwargs:
            product_id = kwargs['product_id']
        else:
            product_id = kwargs['pk']
        bpcode=Product.objects.get(pk=product_id).bpcode
        existing_bom=Bom.objects.filter(bpcode__exact=bpcode)
        existing_bom.delete()
        response_data=self.post(request, **kwargs).data
        response_data['message']= 'BOM updated successfully'
        print(response_data)
        return Response(response_data,status=status.HTTP_201_CREATED)
    # deletion function 
    def delete(self,request,*args, **kwargs):
        if 'product_id' in kwargs:
            product_id = kwargs['product_id']
        else:
            product_id = kwargs['pk']
        bpcode=Product.objects.get(pk=product_id).bpcode
        Bom_instances=Bom.objects.filter(bpcode__exact=bpcode)
        if len(Bom_instances)==0:
            return Response('Bom is not found, invalid bpcode',status=status.HTTP_404_NOT_FOUND)
            
        Bom_instances.delete()
        return Response("Bom deleted successfully ",status=status.HTTP_200_OK)
    
            
        
        
        
        
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
            stock_instance.qty += int(qty)
            stock_instance.save()

            #  add_stock_log is a function that logs the stock addition
            log = add_stock_log({'matcode': matcode, 'qty': qty, 'Add_or_Consumed': "ADDED",
                                 'Date': data.get('Date'), 'gnr_no': data.get('grn_no'), 'srn_no': data.get('snr_no'), 'remark': data.get('remark')})
            return Response({'Success': 'Stock added successfully', 'log': log},
                            status=status.HTTP_200_OK)
        except Stock.DoesNotExist:
            return Response({'Error': 'Stock does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)
    # adding new element to the stock

    def post(self, request, *args, **kwargs):
        Serializer = self.get_serializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return JsonResponse({'success': Serializer.data})
    # gives the list of stocks of all material

    def get(self, request, *args):
        stock_instance = self.queryset.all()
        serializer = Stock_Serializer(stock_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NotifyLimitAPI(APIView):
    serializer_class = Stock_Serializer
    queryset = Stock.objects.all()

    def get(self, request, *args):
        stock_instance = self.serializer_class(Stock.objects.filter(
            qty__lt=F('safe_stock')),many=True).data
        return Response({'list': [stock_instance]}, status=status.HTTP_200_OK)



class Material_API(generics.GenericAPIView):
    serializer_class = MaterialSerializer
    pagination_class = MyPagination

    queryset = MaterialList.objects.all()

    def post(self, request, *args, **kwargs):
        Serializer = self.get_serializer(data=request.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.save()
        return JsonResponse({'success': Serializer.data})

    def get(self, request, pk=None):
        if pk:
            obj = MaterialList.objects.get(pk=pk)
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        else:
            page = self.paginate_queryset(self.queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            serializer = self.get_serializer(self.queryset, many=True)
            return Response(serializer.data)


# created function for producing excel sheet of bom
@api_view(['GET'])
def get_file(request, pk):

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'Error_message': "The product does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    serialzer = Product_Serializer(product, many=False).data
    
    bom = BomSerializer(Bom.objects.filter( bpcode__exact=str(serialzer['bpcode'])), many=True).data
    if len(bom) ==0:
        return Response("There not exist any bom for this product",status=status.HTTP_400_BAD_REQUEST)
    items = []
    for each_item in bom:
        material = MaterialSerializer(MaterialList.objects.get(
            pk=each_item['matcode']), many=False).data
        each_item.update({'title': material['title']})
        items.append(each_item)
    return get_excel(data=items, name=product.productname)


@api_view(['GET'])
def product_suggestions(request):
    data=Product.objects.all().values('productid','productname')

    return Response({"Product_ids":data},status=status.HTTP_200_OK)

class Pr_Api(APIView):
    serializer_class=Pr_Serializer
    objects=Prdetail.objects.all()
    
    def get(self, request, pk=None):
        if pk:
            obj = Prdetail.objects.get(pk=pk)
            serializer = self.serializer_class(obj,many=False)
            return Response({"successfully retrived":serializer.data},status=status.HTTP_200_OK)
        else:
            serializer=self.serializer_class(self.objects,many=True)
            return Response({"PR_list":serializer.data},status=status.HTTP_200_OK)
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"successfully pi created":serializer.data},status=status.HTTP_201_CREATED)
        return Response({"error_occured":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
