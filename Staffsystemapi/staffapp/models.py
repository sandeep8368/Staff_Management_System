from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length = 40)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 20)
    password = models.IntegerField()