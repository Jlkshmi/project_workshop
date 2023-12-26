from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_workmanager=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)

# customer table
class Customer(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    lisence_no=models.CharField(max_length=100)
    vehicle_model=models.CharField(max_length=100)

class Workmanager(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    emp_id=models.CharField(max_length=100)