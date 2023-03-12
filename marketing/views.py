
from django.http import JsonResponse
from django.shortcuts import HttpResponse



from rest_framework.decorators import api_view
from .models import Marketing,Item,addresss
from .serializers import MarketingSerializer,ItemSerializer,AddressSerializer
from .deconstruct import Deconstruct
@api_view(['POST'])
def create_order(request):
    
    data=Deconstruct(request.data)
    
    marketing_instance=MarketingSerializer(data=dict(data.marketing_instance()))
 
    buyer_addrs_instance=AddressSerializer(data=data.buyer_addr())
    consign_addrs_instance=AddressSerializer(data=data.consign_address())
    list_of_items=data.item_deconstruct()
     
  
   
    if marketing_instance.is_valid():
        
        marketing_instance.save()
        if buyer_addrs_instance.is_valid() and consign_addrs_instance.is_valid():
            
            buyer_addrs_instance.save()
            consign_addrs_instance.save()
        
        for each_item in list_of_items:
            item_data=dict(each_item)

            item_instance=ItemSerializer(data=item_data)
            
            if item_instance.is_valid():
                
                item_instance.save()
                
            else:
                
                
                
                return JsonResponse(str(item_instance.errors),safe=False)
        
            return JsonResponse(str(marketing_instance.data)+str(buyer_addrs_instance.data)+str(consign_addrs_instance.data),safe=False)
        return JsonResponse(str(buyer_addrs_instance.errors)+str(consign_addrs_instance.errors),safe=False)
        
            
    return JsonResponse(str(marketing_instance.errors),safe=False)

@api_view(['GET'])
def list_order(request):
    all_data=Marketing.objects.all()
    all_marketing_data=MarketingSerializer(all_data,many=True).data
    result=dict()
    marketing_order_list = []
    for each in all_marketing_data:
        marketting_object=dict(each)
        
        buyer_addrs_instance=AddressSerializer(addresss.objects.filter(group_id=each['no'],type='buyer'),many=True).data
        consign_addrs_instance=AddressSerializer(addresss.objects.filter(group_id=each['no'],type='consign'),many=True).data
        

        marketting_object.update({"buyer_addr":buyer_addrs_instance})
        marketting_object.update({"consign_addr":consign_addrs_instance})
        Items=ItemSerializer(Item.objects.filter(item_group=each['no']),many=True).data
        marketting_object.update({"items":Items})        
    
        

        marketing_order_list.append(marketting_object)
    result.update({"oders":marketing_order_list})
    # result=marketing_instance+addrs+Items
    return JsonResponse(result,safe=False)
    
    
@api_view(['PUT'])
def update_order(request,pk):
    all_data=Deconstruct(data=request.data)
    marketing_object=Marketing.objects(id=pk)
    buyer_addrs_object=addresss.objects.filter(no= 'key',type='buyer')
    consign_addrs_object=addresss.objects.filter(no= 'key',type='consign')
    
    
    marketing_instance=MarketingSerializer(instance=marketing_object,data=all_data.marketing())
 
    buyer_addrs_instance=AddressSerializer(instance=buyer_addrs_object,data=all_data.buyer_addr())
    consign_addrs_instance=AddressSerializer(instance=consign_addrs_object,data=all_data.consign_address())
    list_of_items=all_data.item_deconstruct()
    
    #note
    #need to change the validator function in the serializer
    #needed to research
    
    
    if marketing_instance.is_valid():
        
        marketing_instance.save()
        if buyer_addrs_instance.is_valid() and consign_addrs_instance.is_valid():
            
            buyer_addrs_instance.save()
            consign_addrs_instance.save()
        
        for each_item in list_of_items:
            item_data=dict(each_item)

            item_instance=ItemSerializer(data=item_data)
            
            if item_instance.is_valid():
                
                item_instance.save()
                
            else:
                
                
                
                return JsonResponse(str(item_instance.errors),safe=False)
        
            return JsonResponse(str(marketing_instance.data)+str(buyer_addrs_instance.data)+str(consign_addrs_instance.data),safe=False)
        return JsonResponse(str(buyer_addrs_instance.errors)+str(consign_addrs_instance.errors),safe=False)
    
    return JsonResponse("ERROR 500 BAD REQUEST",safe=False)
    
        
    
    
    
    
    
          