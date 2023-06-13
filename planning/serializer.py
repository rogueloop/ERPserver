from rest_framework import serializers
from .models import Prdetail, Prdetaillog, Status, Bom,MaterialList,Product, Stock, Stock_log

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields ='__all__'
 
 
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
    
class Stock_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Stock
        fields='__all__'

class Stock_log_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Stock_log
        fields = ['matcode', 'qty', 'Add_or_Consumed', 'Date', 'grn_no', 'snr_no', 'remark']
        
class Pr_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model= Prdetail
        fields='__all__'

class Prlog_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model =Prdetaillog
        fields='__all__'