from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField()
    contact = models.IntegerField()
    password = models.CharField(max_length=8)
    cpass = models.CharField(max_length=8)
    image = models.ImageField(upload_to='image/')
    document = models.FileField(upload_to='file/')  

    