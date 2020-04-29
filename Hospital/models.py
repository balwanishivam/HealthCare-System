from django.db import models

# Create your models here.

class Hosp_detail(models.Model):
    code=models.CharField(max_length=4,primary_key=True)
    name=models.CharField(max_length=25)
    address=models.CharField(max_length=100)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999),MinValueValidator(1000000)])
    email=models.EmailField(max_length=50)
    emergency_contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999), MinValueValidator(1000000)])
    

class Days(models.Model):
    day = models.CharField(max_length=8)


class Doctor(models.Model):
    name=models.CharField(max_length=25)
    speciality=models.CharField(max_length=20)
    qualification=models.CharField(max_length=10)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    consult_hrs=models.TimeField(auto_now=False, auto_now_add=False)
    working_days= models.ManyToManyField(Days)
    opd_no=models.IntegerField(max_length=3)
    hospital=models.ForeignKey(Hospital)
    
class Patient(models.Model):
    name=models.CharField(max_length=25)
    dob=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=10)
    blood_group=models.CharField(max_length=15)
    med_history=models.CharField()
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    adm_date=models.DateField(auto_now=False, auto_now_add=False)
    discharge_date=models.DateField(auto_now=False, auto_now_add=False)
    
class Tests(models.Model):
    test_id = models.CharField(max_length=5)
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=30)
    cost=models.IntegerField(blank=False)
    
class Conducted(models.Model):
    diagnosis = models.CharField()
    report=models.CharField()
    test=models.ForeignKey(Tests)
    patient=models.ForeignKey(Patient)
    date=models.DateField(auto_now=False, auto_now_add=False)