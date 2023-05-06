from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
    message = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.user.username}: {self.message}"

    class Meta:
        managed = True
        db_table = 'notification'
