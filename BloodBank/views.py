from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

#Index Page
class Index(View):
    template_name='BlookBank/layout.html'

    def get(self,request):
        return render(request,self.template_name)


#Registration 
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

#Donor Details
#Add_Details
class AddDonor(LoginRequiredMixin,View):
    form_class=DonorDetails
    template_name='BloodBank/donor_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            add_bottles=self.request.no_of_units_donated
            blood_group=self.request.blood_group
            blood=Inventory.objects.get(blood_group=blood_group)
            blood.no_of_units=blood.no_of_units+add_bottles
            blood.save()
            provider.save()
            return redirect('bloodbank:view_inventory')
        
        return render(request,self.template_name,{'form':form})

#list Donor
class ViewDonor(ListView):
    template_name='BloodBank/donor.html'
    context_object_name='donors'
    model=Doctor
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#edit donor
class EditDonor(UpdateView):
    model=Doctor
    form_class=DoctorDetails
    template_name='BloodBank/donor_form.html'
    success_url=reverse_lazy('bloodbank:view_donor')

#Delete donor
class DeleteDonor(DeleteView):
    model=Doctor
    success_url=reverse_lazy('bloodbank:view_donor')


#Reciever Views
class AddReceiver(LoginRequiredMixin,View):
    form_class=RecieverDetails
    template_name='BloodBank/receiver_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            add_bottles=self.request.no_of_units_donated
            blood_group=self.request.blood_group
            blood=Inventory.objects.get(blood_group=blood_group)
            blood.no_of_units=blood.no_of_units-add_bottles
            blood.save()
            provider.save()
            return redirect('BloodBank:view_inventory')
        
        return render(request,self.template_name,{'form':form})

#list Reciever
class ViewReciever(ListView):
    template_name='BloodBank/reciever.html'
    context_object_name='recievers'
    model=Doctor
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#edit reciever
class EditDonor(UpdateView):
    model=Doctor
    form_class=DoctorDetails
    template_name='BloodBank/reciever_form.html'
    success_url=reverse_lazy('bloodbank:view_reciever')

#Delete reciever
class DeleteDonor(DeleteView):
    model=Doctor
    success_url=reverse_lazy('bloodbank:view_reciever')


# Inventory views
#Add Inventory
class AddInventory(LoginRequiredMixin,View):
    form_class=BloodInventory
    template_name='BloodBank/inventory_form.html'

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

#list Reciever
class ViewInvenotry(ListView):
    template_name='BloodBank/inventory.html'
    context_object_name='recievers'
    model=Doctor
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#edit reciever
class EditInventory(UpdateView):
    model=Doctor
    form_class=DoctorDetails
    template_name='BloodBank/inventory_form.html'
    success_url=reverse_lazy('bloodbank:view_reciever')

#Delete reciever
class DeleteInventory(DeleteView):
    model=Doctor
    success_url=reverse_lazy('bloodbank:view_reciever')




# Create your views here.
