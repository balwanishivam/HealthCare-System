from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
import datetime
from BloodBank.models import City

#Store Details
class Store_Details(models.Model):
    code=models.CharField(max_length=4,primary_key=True)
    name=models.CharField(max_length=100)
    street_no=models.CharField(max_length=100)
    area_name=models.CharField(max_length=100)
    distance_from_city_center=models.IntegerField(max_length=20)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    pincode=models.IntegerField(max_length=6)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])

#Company Name
class Company(models.Model):
    code=models.CharField(max_length=4,primary_key=True)
    name=models.CharField(max_length=100)
    street_no=models.CharField(max_length=100)
    area_name=models.CharField(max_length=100)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    pincode=models.IntegerField(max_length=6)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])

#Medicine Inventory
class Medicine_Inventory(models.Model):
    store_name=models.ForeignKey(Store_Details,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)
    med_type=models.CharField(max_length=120)
    mdf=models.DateField()
    expiry=models.DateField(),
    


# Create your models here.
