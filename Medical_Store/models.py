from django.db import models
from myuser.models import Myuser,City
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
import datetime
from BloodBank.models import City

#Store Details
class Store_Details(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    distance_from_city_center=models.IntegerField()
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)

#Company Name
class Company(models.Model):
    code=models.CharField(max_length=4,primary_key=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)


#Medicine Inventory
class Medicine_Inventory(models.Model):
    name=models.CharField(max_length=200)
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)
    mdf=models.DateField()
    expiry=models.DateField()
    mrp=models.PositiveIntegerField()
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)



# Create your models here.
