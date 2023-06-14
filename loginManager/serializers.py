from rest_framework import serializers
from django.contrib.auth.models import User
from .models import department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    department = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username','password', 'department')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        department_data = validated_data.pop('department')
        user = User.objects.create_user(**validated_data)
        department.objects.create(user=user, department=department_data)
        return user
