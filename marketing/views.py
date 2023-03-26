
from django.http import JsonResponse
from requests import Response

from rest_framework import status

from .procedure import delete_current_model, get_status,add_status,delete_current_marketing
from rest_framework.decorators import api_view
from .models import Marketing,Item,addresss
from .serializers import MarketingSerializer,ItemSerializer,AddressSerializer
from .deconstruct import Deconstruct

#added logger





@api_view(['POST'])
def create_order(request):
    print("enter the post")
    
    data=Deconstruct(request.data)
    
    marketing_instance=MarketingSerializer(data=dict(data.marketing()))
 
    buyer_addrs_instance=AddressSerializer(data=data.buyer_addr())
    consign_addrs_instance=AddressSerializer(data=data.consign_address())
    list_of_items=data.item_deconstruct()
     
  
   
    if marketing_instance.is_valid():
        
        marketing_instance.save()
        if buyer_addrs_instance.is_valid() and consign_addrs_instance.is_valid():
            
            
            buyer_addrs_instance.save()
            consign_addrs_instance.save()
            flag=False
            for each_item in list_of_items:
                item_data=dict(each_item)

                item_instance=ItemSerializer(data=item_data)
                
            
                if item_instance.is_valid():
                
                    item_instance.save()
                    flag=True
                else:
                    delete_current_model(request.data["woso_no"],flag=flag)
                    
                    return JsonResponse(str(item_instance.errors),safe=False)
        
            return JsonResponse(request.data,safe=False,status=status.HTTP_201_CREATED)
        else:
            delete_current_marketing(request.data["woso_no"])
            
            return JsonResponse(str(buyer_addrs_instance.errors + "\n")+str(consign_addrs_instance.errors),status=status.HTTP_400_BAD_REQUEST,safe=False)
        
    print("error in post")
    message=str(marketing_instance.errors)
    print(marketing_instance.errors)
    return Response(message,status=status.HTTP_400_BAD_REQUEST,safe=False)

@api_view(['GET'])
def list_order(request):
    all_data=Marketing.objects.all()
    print("someone has requested data")
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
        marketting_object.update({"status":get_status(marketting_object['no'])})        
    
        

        marketing_order_list.append(marketting_object)
    result.update({"oders":marketing_order_list})
    # result=marketing_instance+addrs+Items
    return JsonResponse(result,safe=False)
    
    
@api_view(['PUT'])
def update_order(request,pk):
    all_data=Deconstruct(data=request.data) #data
    marketing_object_to_update=Marketing.objects(id=pk) #marketing instance
    buyer_addrs_object=addresss.objects.filter(group_id= pk,type='buyer')
    consign_addrs_object=addresss.objects.filter(group_id= pk,type='consign')
    
    
    marketing_instance=MarketingSerializer(instance=marketing_object_to_update,data=all_data.marketing())
 
    buyer_addrs_instance=AddressSerializer(instance=buyer_addrs_object,data=all_data.buyer_addr())
    consign_addrs_instance=AddressSerializer(instance=consign_addrs_object,data=all_data.consign_address())
    list_of_items=all_data.item_deconstruct()
    
    #note
    #need to change the validator function in the serializer
  
    
    
    if marketing_instance.is_valid():   #needed to research
        
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
        
            return JsonResponse(request.data,safe=False)
        return JsonResponse(str(buyer_addrs_instance.errors)+str(consign_addrs_instance.errors),safe=False)
    
    return JsonResponse(marketing_instance.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_order(request,id):
    Items=Item.objects.filter(item_group=id)
    Items.delete()
    addresses=addresss.objects.filter(group_id=id)
    addresses.delete()
    marketing_instance=Marketing.objects.filter(no=id)
    marketing_instance.delete()
    return JsonResponse({'message': 'The order is deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
# the function return the status of the order

@api_view(['GET'])
def status(pk):
    return get_status(pk=pk)   
        
    

    
    
    
    
          