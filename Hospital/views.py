from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

#User Registration Details
class UserCreate(LoginRequiredMixin,View):
    form_class=HospDetail
    template_name='Hospital/register.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            print(provider.name)
            provider.user = self.request.user
            provider.save()
            return redirect('Hospital:index')
        
        return render(request,self.template_name,{'form':form})

# Index views
class Index(View):
    template_name='Hospital/layout.html'

    def get(self,request):
        return render(request,self.template_name)


#Doctor's Views
#Add Doctor's details
class AddDoctor(LoginRequiredMixin,View):
    form_class=DoctorDetails
    template_name='Hospital/doctor_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return redirect('Hospital:index')
        
        return render(request,self.template_name,{'form':form})

#View Doctor
class ViewDoctor(ListView):
    template_name='Hospital/doctor.html'
    context_object_name='doctors'
    model=Doctor
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#Edit Doctor(still to be updated)
class EditDoctor(UpdateView):
    model=Doctor
    form_class=DoctorDetails
    template_name='Hospital/doctor_form.html'
    success_url=reverse_lazy('Hospital:view_doctor')

#Delete Doctor
class DeleteDoctor(DeleteView):
    model=Doctor
    success_url=reverse_lazy('Hospital:view_doctor')

#Patient Record
# Add Patient's Records
class AddPatient(LoginRequiredMixin,View):
    form_class=PatientDetails
    template_name='Hospital/patient_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Patient record added sucessfully</html>")
        
        return render(request,self.template_name,{'form':form})

#View Patient
class ViewPatient(ListView):
    template_name='Hospital/patient.html'
    context_object_name='patients'
    model=Patient
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#Edit Patient(still to be updated)
class EditPatient(UpdateView):
    model=Patient
    form_class=PatientDetails

#Delete Patient
class DeletePatient(DeleteView):
    model=Patient
    success_url=reverse_lazy('Hospital:view_patient')

# Test Available
# Test details
class AddTest(LoginRequiredMixin,View):
    form_class=TestDetails
    template_name='Hospital/test_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Test Added Successfully</html>")
        
        return render(request,self.template_name,{'form':form})

#View Tests
class ViewTest(ListView):
    template_name='Hospital/test.html'
    context_object_name='tests'
    model=Tests
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#Edit Tests(still to be updated)
class EditTest(UpdateView):
    model=Tests
    form_class=TestDetails

#Delete Tests
class DeleteTest(DeleteView):
    model=Tests
    success_url=reverse_lazy('Hospital:view_test')


#Test Conducted
# Patient Test Conducted 
class AddConducted(LoginRequiredMixin,View):
    form_class=TestConducted
    template_name='Hospital/conducted_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Test Conducted Added Succesfully</html>")
        
        return render(request,self.template_name,{'form':form})

#View Conducted
class ViewConducted(ListView):
    template_name='Hospital/conducted.html'
    context_object_name='conducted'
    model=Conducted
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#Edit Conducted(still to be updated)
class EditConducted(UpdateView):
    model=Conducted
    form_class=TestConducted

#Delete Conducted
class DeleteConducted(DeleteView):
    model=Conducted
    success_url=reverse_lazy('Hospital:view_conducted')

# Create your views here.
