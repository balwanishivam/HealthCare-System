
from django import forms
from .models import Donor,Reciever,BB_Details,Blood_Inventory


class BBDetails(forms.ModelForm):
    class Meta:
        model= BB_Details
        fields=['name','address','city','pincode','contact','user']
        exclude=('user',)

class DonorDetails(forms.ModelForm):
    class Meta:
        model=Donor
        fields=['name','contact','email','area','blood_group','date','no_of_units_donated','user']
        exclude=('user',)

class RecieverDetails(forms.ModelForm):
    class Meta:
        model=Reciever
        fields=['name','contact','email','blood_group','date','no_of_units_recieved','user']
        exclude=('user',)

class BloodInventory(forms.ModelForm):
    class Meta:
        model=Blood_Inventory
        fields=['blood_group','no_of_units','user']
        exclude=('user',)

