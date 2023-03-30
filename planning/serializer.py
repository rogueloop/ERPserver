from rest_framework import serializers
from .models import Status, Bom

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        
        fields = ['work_order_no']
 
 
class BomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bom
        fields = '__all__'