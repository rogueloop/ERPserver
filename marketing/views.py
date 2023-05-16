from rest_framework import status,generics
from rest_framework.decorators import api_view, APIView
from .models import Marketing, Item, addresss
from .serializers import MarketingSerializer, ItemSerializer, AddressSerializer
from planning.models import Status
from rest_framework.response import Response
from planning.serializer import StatusSerializer


class MarketingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Marketing.objects.all()
    serializer_class = MarketingSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        marketing_instance = serializer.save()
        status_instance = Status.objects.create(work_order_no=marketing_instance)
        response_data = serializer.data.copy()
        response_data.update({'status': status_instance.status})
      
        return Response(response_data)
 
class MarketingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marketing.objects.all()
    serializer_class = MarketingSerializer

    def get(self,request, *args, **kwargs):
        marketing_instance = self.get_object()
        serializer = self.serializer_class(marketing_instance)
        status_instance = Status.objects.get(work_order_no=marketing_instance)
        response_data = serializer.data
        response_data.update({'status': status_instance.status})
        items = Item.objects.filter(item_group=marketing_instance)
        items_serializer = ItemSerializer(items, many=True)
        address=AddressSerializer(addresss.objects.filter(group=marketing_instance),many=True).data
        response_data.update({'address':address})
        response_data.update({'items': items_serializer.data})
        return Response(response_data)

class ItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    


class ItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AddressListCreateAPIView(generics.ListCreateAPIView):
    queryset = addresss.objects.all()
    serializer_class = AddressSerializer


class AddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = addresss.objects.all()
    serializer_class = AddressSerializer

class StatusAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
  

@api_view(['GET'])
def order_suggestions(request):
    data=Marketing.objects.values('no')
    return Response(data,status=status.HTTP_202_ACCEPTED)        