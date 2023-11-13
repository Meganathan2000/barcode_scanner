from django.db import models

# Create your models here.
class data(models.Model):
    
    barcode = models.CharField(max_length=50)
    
    