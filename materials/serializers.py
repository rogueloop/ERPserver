from rest_framework import serializers


from.models import Po,Polog




class Po_Serializer(serializers.ModelSerializer):


    class Meta:


        model = Po


        fields = '__all__'
    


class Polog_Serializer(serializers.ModelSerializer):


    class Meta:


        model = Polog


        fields = '__all__'
        