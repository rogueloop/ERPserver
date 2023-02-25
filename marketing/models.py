from django.db import models

# Create your models here.

class Order(models.Model):
    Customer = models.CharField(max_length=50)
