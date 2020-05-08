from .models import *
from django import forms

class HospDetail(forms.ModelForm):
    class Meta:
        fields = ['code', 'name', 'address', 'contact', 'email', 'emergency_contact', 'user']
        
class Doctor(forms.ModelForm):
    class Meta:
        fields = ['name', 'speciality', 'qualification', 'contact', 'consult_hrs', 'working_days', 'opd_no', 'hospital', 'user']
        
        
class Patient(forms.ModelForm):
    class Meta:
        fields = ['name', 'dob', 'gender', 'bloog_group', 'med_history', 'contact', 'adm_date', 'discharge_date', 'user']
        exclude=('user',)
        
class Tests(forms.ModelForm):
    class Meta:
        fields = ['test_id', 'report', 'test', 'patient', 'date']
        exclude = ('user',)

class Conducted(forms.ModelForm):
    class Meta:
        fields = ['diagnosis', 'report', 'test', 'patient', 'date']
        exclude = ('user',)