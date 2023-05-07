from django.test import TestCase

# Create your tests here.
from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message', 'recipient']
        
