from django.db import models
from django import forms

# Create your models here.
class Users_Authrization(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Date_and_Time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Username
    