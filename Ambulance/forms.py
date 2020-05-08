from django import forms
from .models import *

class ServiceProvider(forms.ModelForm):
    class Meta:
        model = Service_Provider
        fields=['name', 'city', 'street_no', 'area_name', 'pincode', 'no_of_ambulances', 'contact', 'user']
        
class AmbulanceDetails(forms.ModelForm):
    class Meta:
        model = Ambulance_Details
        fields=['vehicle_no', 'org_name', 'name', 'city', 'pincode', 'contact', 'amb_type', 'user']
        exclude=('user',)
