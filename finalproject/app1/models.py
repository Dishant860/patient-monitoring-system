from enum import unique
from django.db import models
from datetime import date


# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=10)
    email=models.EmailField(default='')
    password=models.CharField(max_length=10,default='')

    def __str__(self):
        return self.email

class Addmedicinenew(models.Model):
    medicinename=models.CharField(max_length=100)
    medicineuse=models.CharField(max_length=100)
    
    def __str__(self):
        return self.medicinename
        