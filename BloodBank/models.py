from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from myuser.models import Myuser,City
import datetime

BLOOD_GROUP=[
    ('A+','A+'),
    ('B+','B+'),
    ('O+','O+'),
    ('AB+','AB+'),
    ('A-','A-'),
    ('B-','B-'),
    ('O-','O-'),
    ('AB-','AB-'),
]

#BB-Details
class BB_Details(models.Model):
        
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.ForeignKey(City,on_delete=models.DO_NOTHING)
    pincode=models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

#Blood INventory
class Blood_Inventory(models.Model):
    blood_group=models.CharField(max_length=3,choices=BLOOD_GROUP,unique=True)
    no_of_units=models.IntegerField(default=0)
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)

#Donor Details
class Donor(models.Model):
    name=models.CharField(max_length=100)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    email=models.EmailField(max_length=256)
    area=models.CharField(max_length=200)
    blood_group=models.CharField(max_length=3,choices=BLOOD_GROUP)
    date=models.DateField( default=datetime.date.today)
    no_of_units_donated=models.IntegerField(default=1)
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)


#Reciever Model
class Reciever(models.Model):
    name=models.CharField(max_length=100)
    contact=models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    email=models.EmailField(max_length=256)
    blood_group=models.CharField(max_length=3,choices=BLOOD_GROUP)
    date=models.DateField(default=datetime.date.today)
    no_of_units_recieved=models.IntegerField(default=1)
    user=models.ForeignKey(Myuser,on_delete=models.CASCADE)

# Create your models here.
