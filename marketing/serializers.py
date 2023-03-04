from rest_framework import serializers
from .models import Marketing,Item,addresss

class MarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing
        
        fields = '__all__'
 
 
        
class ItemSerializer(serializers.ModelSerializer):
       class Meta:
        model=Item
        fields='__all__'
    
class AddressSerializer(serializers.ModelSerializer):
       class Meta:
        model=addresss
        fields='__all__'
        
    