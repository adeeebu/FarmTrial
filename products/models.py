from django.db import models

# Create your models here.

class FarmProduct(models.Model):
    prod_id = models.IntegerField()
    prod_type = models.CharField(max_length = 50)
    prod_name = models.CharField(max_length = 100)
    prod_price = models.FloatField()
    prod_brand = models.CharField(max_length = 50)
    prod_link = models.URLField(max_length = 200)

    def __str__(self):
    	return self.prod_name 

    
