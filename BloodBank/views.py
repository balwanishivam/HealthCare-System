from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse

from django.contrib.auth.mixins import LoginRequiredMixin

BLOOD_GROUP=[
    ('A+','A+'),
    ('B+','B+'),
    ('O+','O+'),
    ('AB+','AB+'),
    ('A-','A-'),
    ('B-','B-'),
    ('O-','O-'),
    ('AB-','AB-'),
]

#Index Page
class Index(View):
    template_name='BloodBank/layout.html'

    def get(self,request):
        return render(request,self.template_name)


#Registration 
class UserCreate(LoginRequiredMixin,View):
    form_class=BBDetails
    template_name='BloodBank/register.html'

    def initialise(self):
        for i in range(len(BLOOD_GROUP)) :
            print(i)
            blood=Blood_Inventory()
            blood.blood_group=BLOOD_GROUP[i]
            blood.no_of_units=0
            blood.user=self.request.user
            blood.save()
            
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            initialise()
            return redirect('bloodbank:index')
        
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
            provider.save()
            print(provider.blood_group)
            blood=get_object_or_404(Blood_Inventory,blood_group=provider.blood_group)
            blood.no_of_units=blood.no_of_units+provider.no_of_units_donated
            blood.save()
            return redirect('bloodbank:view_inventory')
        
        return render(request,self.template_name,{'form':form})


#list Donor
class ViewDonor(ListView):
    template_name='BloodBank/donor.html'
    context_object_name='donors'
    model=Donor
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#edit donor
class EditDonor(UpdateView):
    model=Donor
    form_class=DonorDetails
    template_name='BloodBank/donor_form.html'
    success_url=reverse_lazy('bloodbank:view_donor')

#Delete donor
class DeleteDonor(DeleteView):
    model=Donor
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
            blood_group=form.instance.blood_group
            required=form.instance.no_of_units_recieved
            blood=get_object_or_404(Blood_Inventory,blood_group=blood_group)
            if(blood.no_of_units>=required):
                print("1")
                blood.no_of_units=blood.no_of_units-required
                blood.save()
                provider=form.save(commit=False)
                form.instance.user = self.request.user
                provider.save()
                return redirect('bloodbank:view_inventory')
            else:
                return render(request,self.template_name,{'form':form})
        return render(request,self.template_name,{'form':form})

#list Reciever
class ViewReceiver(ListView):
    template_name='BloodBank/receiver.html'
    context_object_name='receivers'
    model=Reciever
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#edit reciever
class EditReceiver(UpdateView):
    model=Reciever
    form_class=RecieverDetails
    template_name='BloodBank/receiver_form.html'
    success_url=reverse_lazy('bloodbank:view_receiver')

#Delete reciever
class DeleteReceiver(DeleteView):
    model=Reciever
    success_url=reverse_lazy('bloodbank:view_receiver')


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
            return redirect('bloodbank:view_inventory')
        return render(request,self.template_name,{'form':form})

    

#list Reciever
class ViewInventory(ListView):
    template_name='BloodBank/inventory.html'
    context_object_name='inventory'
    model=Blood_Inventory
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)

#edit reciever
class EditInventory(UpdateView):
    model=Blood_Inventory
    form_class=BloodInventory
    template_name='BloodBank/inventory_form.html'
    success_url=reverse_lazy('bloodbank:view_inventory')

#Delete reciever
class DeleteInventory(DeleteView):
    model=Blood_Inventory
    success_url=reverse_lazy('bloodbank:view_inventory')




# Create your views here.
