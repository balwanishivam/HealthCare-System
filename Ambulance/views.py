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
    template_name='Ambulance/layout.html'

    def get(self,request):
        return render(request,self.template_name)


class UserCreate(LoginRequiredMixin,View):
    form_class=ServiceProvider
    template_name='Ambulance/register.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            provider.user = self.request.user
            provider.save()
            return redirect("Ambulance:index")
        
        return render(request,self.template_name,{'form':form})

class AddAmbulance(LoginRequiredMixin,View):
    form_class=AmbulanceDetails
    template_name='Ambulance/ambulance_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            provider=form.save(commit=False)
            provider.user = self.request.user
            provider.save()
            #redirect to home page
            return redirect("Ambulance:view_ambulance")
        
        return render(request,self.template_name,{'form':form})

#View Doctor
class ViewAmbulance(ListView):
    template_name='Ambulance/ambulance.html'
    context_object_name='ambulance_details'
    model=Ambulance
    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user is None:
            return qs
        return qs.filter(user=user)


class EditAmbulance(UpdateView):
    model=Ambulance
    form_class=AmbulanceDetails
    template_name='Ambulance/ambulance_form.html'
    success_url=reverse_lazy('Ambulance:view_ambulance')

#Delete Doctor
class DeleteAmbulance(DeleteView):
    model=Ambulance
    success_url=reverse_lazy('Ambulance:view_ambulance')

# Create your views here.
