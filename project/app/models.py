from django.db import models
# Create your models here.
class Student(models.Model):
    name=models.TextField()
    age=models.IntegerField()
    rollno=models.IntegerField()