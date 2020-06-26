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
    template_name='Medical_Store/layout.html'

    def get(self,request):
        return render(request,self.template_name)


class UserCreate(LoginRequiredMixin,View):
    form_class=StoreDetails
    template_name='Medical_Store/register.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return redirect('Medical_Store:index')
        
        return render(request,self.template_name,{'form':form})


class AddCompany(LoginRequiredMixin,View):
    form_class=CompanyDetails
    template_name='Medical_Store/add_company.html'
    #add_company.html ka template nahi bana hua

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return HttpResponse("<html>Company Added successfully</html>")
        
        return render(request,self.template_name,{'form':form})


class AddMedicine(LoginRequiredMixin,View):
    form_class=MedicineInventory
    template_name='Medical_Store/medicine_inventory_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            form.instance.user = self.request.user
            provider.save()
            return redirect('Medical_Store:view_medicine_inventory')
        
        return render(request,self.template_name,{'form':form})


#list medicines
class ViewMedicine(ListView):
    template_name='Medical_Store/medicine_inventory.html'
    context_object_name='medicine_inventory'
    model=Medicine_Inventory
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)


#edit medicine_inventory
class EditMedicine(UpdateView):
    model=Medicine_Inventory
    form_class=MedicineInventory
    template_name='Medical_Store/medicine_inventory_form.html'
    success_url=reverse_lazy('Medical_Store:view_medicine_inventory')

#Delete medicine_inventory
class DeleteMedicine(DeleteView):
    model=Medicine_Inventory
    success_url=reverse_lazy('Medical_Store:view_medicine_inventory')


# Create your views here.
