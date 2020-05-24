from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

class UserCreate(LoginRequiredMixin,View):
    form_class=BBDetails
    template_name='BloodBank/register.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Welcome to Blood bank</html>")
        
        return render(request,self.template_name,{'form':form})

class AddDonor(LoginRequiredMixin,View):
    form_class=DonorDetails
    template_name='BloodBank/add_donor.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Donor added successfully</html>")
        
        return render(request,self.template_name,{'form':form})

class AddReceiver(LoginRequiredMixin,View):
    form_class=RecieverDetails
    template_name='BloodBank/add_receiver.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Receiver added successfully</html>")
        
        return render(request,self.template_name,{'form':form})


class Inventory(LoginRequiredMixin,View):
    form_class=BloodInventory
    template_name='BloodBank/inventory.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Donor added successfully</html>")
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


# Create your views here.
