
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Notification
from .serializers import NotificationSerializer


class NotificationAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        notification = serializer.save(sender=request.user)
        return Response({'id': notification.id})
