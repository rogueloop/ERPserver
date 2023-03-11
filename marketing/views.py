
from django.http import JsonResponse
from django.shortcuts import HttpResponse



from rest_framework.decorators import api_view
from .models import Marketing,Item,addresss
from .serializers import MarketingSerializer,ItemSerializer,AddressSerializer
from .deconstruct import Deconstruct
@api_view(['POST'])
def create_order(request):
    
    data=Deconstruct(request.data)
    
    marketing=MarketingSerializer(data=dict(data.marketing()))
 
    add_buyer=AddressSerializer(data=data.buyer_addr())
    add_consign=AddressSerializer(data=data.consign_address())
    items=data.item_deconstruct()
     
  
   
    if marketing.is_valid():
        
        marketing.save()
        if add_buyer.is_valid() and add_consign.is_valid():
            
            add_buyer.save()
            add_consign.save()
        
        for i in items:
            d=dict(i)

            item=ItemSerializer(data=d)
            
            if item.is_valid():
                
                item.save()
                
            else:
                
                
                return HttpResponse(item.errors)
        
        return JsonResponse(str(marketing.data)+str(add_buyer.data)+str(add_consign.data),safe=False)
        
        
            
    return HttpResponse("ERROR 500")

@api_view(['GET'])
def list_order(request):
    marketing=Marketing.objects.all()
    mark=MarketingSerializer(marketing,many=True).data
    result=dict()
    
    for i in mark:
        thing=dict(i)
        
        add_buyer=AddressSerializer(addresss.objects.filter(group_id=i['no'],type='buyer'),many=True).data
        add_consign=AddressSerializer(addresss.objects.filter(group_id=i['no'],type='consign'),many=True).data
        
       
        thing.update({"buyer_addr":add_buyer})
        thing.update({"consign_addr":add_consign})
        Items=ItemSerializer(Item.objects.filter(item_group=i['no']),many=True).data
        thing.update({"items":Items})        
    
        
        result.update({thing['no']:thing})
        
    
    # result=marketing+addrs+Items
    return JsonResponse(result,safe=False)
    
    
        
    
        
    
    
    
    
    
          