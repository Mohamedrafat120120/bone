from django.db import models

# Create your models here.
class Patients_Data(models.Model):
    s=[('Male','Male'),('Fmale','Fmale')]
    Patient_Name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=11)
    Address=models.TextField(default='Address')
    Patients_info=models.TextField(default='IFO')
    Type=models.CharField(max_length=100,choices=s)
    Ray=models.ImageField(default="",upload_to='photos%y/%m/%d')
    Date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.Patient_Name