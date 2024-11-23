from django.db import models

# Create your models here.

class Page_Visit(models.Model):
    
    path =models.TextField(blank=True,null=True)
    timestamp = models.TimeField(auto_now=True)
    