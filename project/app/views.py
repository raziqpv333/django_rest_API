from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from .models import*
from .serializers import*
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins


def fun1(req):
    d={'name':'anu','age':22}
    return JsonResponse(d)

def fun2(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=sample(d,many=True)
        return JsonResponse(s.data,safe=False)
@csrf_exempt
def fun3(req):
    if req.method=='GET':
        d=Student.objects.all()
        s=model_serializer(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=model_serializer(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
@csrf_exempt       
def fun4(req,d):
    try:
        demo=Student.objects.get(pk=d)      
    except Student.DoesNotExist:  
        return HttpResponse('invalid')
    if req.method=='GET':
        s=model_serializer(demo)
        return JsonResponse(s.data)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=model_serializer(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors) 
    elif req.method=='DELETE':
        demo.delete()
        return HttpResponse('deleted')               


@api_view(['GET','PUT','DELETE'])
def fun6(req,d):
    try:
        demo=Student.objects.get(pk=d)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=model_serializer(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=model_serializer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_NOT_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class fun7(APIView):
    def get(self,req):
        demo=Student.objects.all()
        s=model_serializer(demo,many=True)
        return Response(s.data)
    def post(self,req):
        s=model_serializer(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)

class fun8(APIView):
    def get(self,req,d):
        try:
            demo=Student.objects.get(pk=d)
            s=model_serializer(demo)
            return Response(s.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

def put(self,req,d):
    try:
        demo=Student.objects.get(pk=id)
        s=model_serializer(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data) 
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST) 
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
                     
