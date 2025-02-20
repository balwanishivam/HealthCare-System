from .models import *
from django import forms
from django.forms import widgets

class TimeInput(forms.TimeInput):
    input_type="time"

class HospDetail(forms.ModelForm):
    class Meta:
        model=Hosp_detail
        fields = ['name', 'address','city','pincode','contact', 'email', 'emergency_contact', 'user']
        exclude=('user',)



class DoctorDetails(forms.ModelForm):
    widgets={'day':forms.CheckboxSelectMultiple}
    contact =forms.CharField(max_length=10)
    starting_time=forms.TimeField(widget=TimeInput)
    ending_time=forms.TimeField(widget=TimeInput)
    class Meta:
        model=Doctor
        fields = ['name', 'speciality', 'qualification', 'contact', 'starting_time','ending_time', 'working_days', 'user']
        exclude=('user',)



class PatientDetails(forms.ModelForm):
    class Meta:
        model=Patient
        fields = ['name', 'dob', 'gender', 'blood_group', 'med_history', 'contact', 'adm_date', 'discharge_date', 'user']
        exclude=('user',)
        
class TestDetails(forms.ModelForm):
    class Meta:
        model=Tests
        fields = ['test_id', 'name', 'test_type', 'cost', 'user']
        exclude = ('user',)

class TestConducted(forms.ModelForm):
    class Meta:
        model=Conducted
        fields = ['diagnosis', 'report', 'test', 'patient', 'date','user']
        exclude = ('user',)