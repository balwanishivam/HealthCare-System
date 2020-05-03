from django.db import models
from BloodBank.models import City
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
import datetime

AMB_CHOICES=(
    ('MAB','Mini Ambulance'),
    ('FAB','Fully Equiped Ambulance'),
)
# Service Provider
class Service_Provider(models.Model):
    name=models.CharField(max_length=256)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    street_no=models.CharField(max_length=100)
    area_name=models.CharField(max_length=100)
    pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    no_of_ambulances=models.IntegerField(default=1)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])

#Ambulance Details
class Ambulance_Details(models.Model):
    vehicle_no=models.CharField(max_length=15,primary_key=True)
    org_name=models.ForeignKey(Service_Provider,on_delete=models.CASCADE)
    name=models.CharField(max_length=256)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    # street_no=models.CharField(max_length=100)
    # area_name=models.CharField(max_length=100)
    pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    amb_type=models.CharField(max_length=3,choices=AMB_CHOICES)



# Create your models here.
