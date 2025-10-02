from rest_framework import serializers
from insurance import models
class StudentSerialzers(serializers.ModelSerializer):
    class Meta:
        model=models.student
        fields="__all__"
