from .models import *
from django import forms

class HospDetail(forms.ModelForm):
    class Meta:
        model=Hosp_detail
        fields = ['name', 'address', 'contact', 'email', 'emergency_contact', 'user']
        exclude=('user',)

class DoctorDetails(forms.ModelForm):
    class Meta:
        model=Doctor
        fields = ['name', 'speciality', 'qualification', 'contact', 'consult_hrs', 'working_days', 'user']
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