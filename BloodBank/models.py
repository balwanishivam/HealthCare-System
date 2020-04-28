from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
import datetime

#City Model
class City(models.Model):
    std_code=models.IntegerField(max_length=5,primary_key=True)
    name=models.CharField(max_length=100)
    city_center=models.CharField(max_length=100)

#BB-Details
class BB_Details(models.Model):
    code=models.CharField(max_length=4,primary_key=True)
    name=models.CharField(max_length=100)
    street_no=models.CharField(max_length=100)
    area_name=models.CharField(max_length=100)
    distance_from_city_center=models.IntegerField(max_length=20)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    pincode=models.IntegerField(max_length=6)

#Blood INventory
class Blood_Inventory(models.Model):
    blood_group=models.CharField(max_length=5,primary_key=True)
    no_of_units=models.IntegerField(default=0)

#Donor Details
class Donor(models.Model):
    name=models.CharField(max_length=100)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    email=models.EmailField(max_length=256)
    blood_group=models.CharField(max_length=5,null=False)
    date=models.DateField( default=datetime.date.today)
    no_of_units_donated=models.IntegerField(default=1)

#Reciever Model
class Reiever(models.Model):
    name=models.CharField(max_length=100)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    email=models.EmailField(max_length=256)
    blood_group=models.CharField(max_length=5,null=False)
    date=models.DateField( default=datetime.date.today)
    no_of_units_recieved=models.IntegerField(default=1)






# Create your models here.
