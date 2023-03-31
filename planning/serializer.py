from rest_framework import serializers
from .models import Status, Bom,MaterialList,Product

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        
        fields = ['work_order_no']
 
 
class BomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bom
        fields = '__all__'
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialList
        fields='__all__'
class Product_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields='__all__'