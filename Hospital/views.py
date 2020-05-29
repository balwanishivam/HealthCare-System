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

# Add Patient's Records
class AddPatient(LoginRequiredMixin,View):
    form_class=PatientDetails
    template_name='Hospital/add_patient.html'

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

# Test details
class AddTest(LoginRequiredMixin,View):
    form_class=TestDetails
    template_name='Hospital/add_test.html'

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

# Patient Test Conducted 
class PatientTest(LoginRequiredMixin,View):
    form_class=TestConducted
    template_name='Hospital/add_conducted.html'

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

class EditDoctor(UpdateView):
    model=Doctor
    form_class=DoctorDetails

class DeleteDoctor(DeleteView):
    model=Doctor
    success_url=reverse_lazy('Hospital:view_doctor')

# Create your views here.
