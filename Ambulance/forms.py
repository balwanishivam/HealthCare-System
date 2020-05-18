from django import forms
from .models import *

class ServiceProvider(forms.ModelForm):
    class Meta:
        model = Service_Provider
        fields=['name', 'city', 'address', 'pincode', 'no_of_ambulances', 'contact', 'user']
        exclude=('user',)
        
class AmbulanceDetails(forms.ModelForm):
    class Meta:
        model = Ambulance_Details
        fields=['vehicle_no', 'org_name', 'name', 'city', 'pincode', 'contact', 'amb_type']
        exclude=('org_name',)
