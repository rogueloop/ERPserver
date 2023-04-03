from rest_framework import serializers
from .models import Status, Bom,MaterialList,Product

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        
        fields = '__all__'
 
 
class BomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bom
        fields = '__all__'
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialList
        fields='__all__'
class Product_Serializer(serializers.ModelSerializer):
    productid = serializers.CharField()
    ssrl = serializers.CharField()
    submited = serializers.BooleanField()
    productname = serializers.CharField()
    db = serializers.BooleanField()
    saeid = serializers.CharField()
    taxid = serializers.CharField()
    model = serializers.CharField()
    netwt = serializers.CharField()
    grosswt = serializers.CharField()
    partno = serializers.CharField()
    standard = serializers.BooleanField()
    bpcode = serializers.CharField()
    
    class Meta:
        model=Product
        fields= ('productid','ssrl', 'submited','productname', 'db', 'saeid', 'taxid', 'model', 'netwt', 'grosswt', 'partno','standard', 'bpcode')