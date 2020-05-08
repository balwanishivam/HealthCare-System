
from django import forms
from .models import City,Donor,Reciever,BB_Details

class CityCreate(forms.ModelForm):
    class Meta:
        model = City
        fields=['std_code','name','city_center']
        

class BBDetails(forms.ModelForm):
    class Meta:
        model= BB_Details
        fields=['code','name','street_no','area_name','distance_from_city_center','city','pincode','contact','user']
        exclude=('user',)

class DonorDetails(forms.ModelForm):
    class Meta:
        model=Donor
        fields=['name','contact','email','blood_group','date','no_of_units','user']
        exclude=('user',)

class RecieverDetails(forms.ModelForm):
    class Meta:
        model=Reciever
        fields=['name','contact','email','blood_group','date','no_of_units','user']
        exclude=('user',)

