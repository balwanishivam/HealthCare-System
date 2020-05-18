from .models import *
from django import forms

class StoreDetails(forms.ModelForm):
    class Meta:
        model=Store_Details
        fields=['name','address','city','pincode','user']
        exclude=('user',)

class CompanyDetails(forms.ModelForm):
    class Meta:
        model=Company
        fields=['code','name','address','city','pincode','contact','user']
        exclude=('user',)

class MedicineInventory(forms.ModelForm):
    class Meta:
        fields=['name','company','mdf','expiry','mrp','user']
        exclude=('user',)

