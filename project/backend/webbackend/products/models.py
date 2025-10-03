from django.db import models

# Create your models here.
class products(models.Model):
    product_id=models.IntegerField(max_length=20,unique=True)
    product_name=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=150,null=True)
    product_price=models.IntegerField(max_length=50,null=False)

    def __str__(self):
        return self.product_name
    