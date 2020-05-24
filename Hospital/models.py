from django.db import models
from myuser.models import Myuser,City
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
import datetime
# Create your models here.

class Hosp_detail(models.Model):
    name=models.CharField(max_length=25)
    address=models.CharField(max_length=500)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    email=models.EmailField(max_length=50)
    emergency_contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)


class Days(models.Model):
    day = models.CharField(max_length=12)

    def __str__(self):
        return self.day


class Doctor(models.Model):
    name=models.CharField(max_length=25)
    speciality=models.CharField(max_length=200)
    qualification=models.CharField(max_length=10)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    starting_time=models.TimeField(auto_now=False, auto_now_add=False)
    ending_time=models.TimeField(auto_now=False, auto_now_add=False)
    working_days= models.ManyToManyField(Days)
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)

    
class Patient(models.Model):
    name=models.CharField(max_length=200)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=10)
    blood_group=models.CharField(max_length=15)
    med_history=models.CharField(max_length=1000)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    adm_date=models.DateField(auto_now=False, auto_now_add=False)
    discharge_date=models.DateField(auto_now=False, auto_now_add=False)  
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    
class Tests(models.Model):
    test_id = models.CharField(max_length=5)
    name=models.CharField(max_length=20)
    test_type=models.CharField(max_length=30)
    cost=models.IntegerField(blank=False)
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    
class Conducted(models.Model):
    diagnosis = models.CharField(max_length=1000)
    report=models.TextField()
    test=models.ForeignKey(Tests,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date=models.DateField(auto_now=False, auto_now_add=False)
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)
