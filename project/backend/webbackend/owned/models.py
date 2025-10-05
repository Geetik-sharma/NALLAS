from django.db import models

# Create your models here.
class owned_products(models.Model):
    owner_name=models.CharField(max_length=20,null=False)
    products=models.CharField(max_length=100,default="empty")
    owner_id=models.IntegerField(null=False)
    def __str__(self):
        return self.owner_name