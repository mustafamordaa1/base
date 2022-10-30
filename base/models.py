from django.db import models
from django.conf import settings

# Create your models here.

class Element(models.Model): 
    name = models.CharField(max_length=128)
    content = models.CharField(max_length=10000)

    def __str__(self):
       return self.name
