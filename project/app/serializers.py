# Create your views here.

from rest_framework import serializers
from .models import*

class sample(serializers.Serializer):
    rollno=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()

class model_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'   