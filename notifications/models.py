from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
    message = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notifications')
    is_read = models.BooleanField(default=False)

    # def __str__(self):
    #     return f"{self.user.username}: {self.message}"

    class Meta:
        managed = True
        db_table = 'notification'
