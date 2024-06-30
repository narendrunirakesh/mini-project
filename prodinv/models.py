from django.db import models

# Create your models here.


class product_adding(models.Model):
    
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_category=models.CharField(max_length=100)
    product_price=models.FloatField(default=0.0)
    
    
    
    