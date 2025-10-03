from django.db import models


# Create your models here.
class employee(models.Model):
    empid=models.IntegerField(max_length=10,unique=True)
    empcon=models.IntegerField(max_length=13,unique=True)
    empname=models.CharField(max_length=15)
    empdep=models.CharField(max_length=40)
    empemail=models.EmailField(unique=True)

    def __str__(self):
        return self.empname