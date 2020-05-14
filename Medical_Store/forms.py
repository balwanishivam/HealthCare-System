
from .models import *
from django import forms

class StoreDeatils(forms.ModelForm):
    class Meta:
        model=Store_Details
        fields=['code','name','street_no','area_name','distance_from_city_center','city','pincode','user']
        exclude=('user',)

class CompanyDetails(forms.ModelForm):
    class Meta:
        model=Company
        fields=['code','name','street_no','area_name','city','pincode','contact']

class MedicineInventory(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['store_name','name','company','med_type','mdf','expiry','user']
        exclude=('user',)

