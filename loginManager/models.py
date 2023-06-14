from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    department=models.CharField(max_length=50)
    
    def __str__(self):
        return self.user;