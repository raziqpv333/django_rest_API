from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def function1(req,):
    a={"name":"arun","age":24}
    return JsonResponse(a)
from rest_framework import serializers
from .models import*

class sample(serializers.serializer):
    roll=serializers.integerfield()
    name=serializers.charfield()
    age=serializers.