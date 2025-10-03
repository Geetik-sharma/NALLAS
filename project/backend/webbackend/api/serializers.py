from rest_framework import serializers
from insurance import models
from employee.models import employee
from products.models import products
class StudentSerialzers(serializers.ModelSerializer):
    class Meta:
        model=models.student
        fields="__all__"


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields="__all__"

class ProdSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields="__all__"