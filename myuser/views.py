from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from Medical_Store.models import * 
from Ambulance.models import *
from BloodBank.models import *
from Hospital.models import *

class Index(View):
    template_name='myuser/home.html'

    def get(self,request):
        return render(request,self.template_name)

class SearchMedicine(View):
    template_name='myuser/search_medicine.html'

    def get(self,request):
        return render(request,self.template_name)

class SearchAmbulance(View):
    template_name='myuser/search_ambulance.html'

    def get(self,request):
        return render(request,self.template_name)

class SearchHospital(View):
    template_name='myuser/search_hopital.html'

    def get(self,request):
        return render(request,self.template_name)

class SearchBloodBank(View):
    template_name='myuser/search_bloodbank.html'

    def get(self,request):
        return render(request,self.template_name)

class ViewMedicine(ListView):
    template_name='myuser/medicine.html'
    context_object_name='medical'
    model=Store_Details
    def get_queryset(self):
        qs = super().get_queryset()
        pincode = self.request.pincode
        if pincode is None:
            return qs
        return qs.filter(pincode=pincode)

class ViewAmbulance(ListView):
    template_name='myuser/ambulance.html'
    context_object_name='ambulance_details'
    model=Service_Provider
    def get_queryset(self):
        qs = super().get_queryset()
        pincode = self.request.pincode
        if pincode is None:
            return qs
        return qs.filter(pincode=pincode)


class ViewHospital(ListView):
    template_name='myuser/hospital.html'
    context_object_name='hospital_details'
    model=Hosp_detail
    def get_queryset(self):
        qs = super().get_queryset()
        pincode = self.request.pincode
        if pincode is None:
            return qs
        return qs.filter(pincode=pincode)


class ViewBloodbank(ListView):
    template_name='myuser/bloodbank.html'
    context_object_name='bb_details'
    model=BB_Details
    def get_queryset(self):
        qs = super().get_queryset()
        pincode = self.request.pincode
        if pincode is None:
            return qs
        return qs.filter(pincode=pincode)

class UserFormView(View):
    form_class=UserForm
    template_name='myuser/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user_type=form.cleaned_data['user_type']
            password2=form.cleaned_data['password2']
            if password==password2:
                user.set_password(password)
                user.save()
                user=authenticate(email=email,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        if user_type=="AMB":
                            return redirect('Ambulance:register')
                        elif user_type=="HSP":
                            return redirect('Hospital:register')
                        elif user_type=="MST":
                            return redirect('Medical_Store:register')
                        elif user_type=="BLB":
                            return redirect('bloodbank:register')
                        else:
                            return render(request,self.template_name,{'form':form})  
            
        form=self.form_class(None)      
        return render(request,self.template_name,{'form':form})

class LoginView(View):
    #use formset and refer sibtc
    form_class=LoginForm
    template_name='myuser/login.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)
        email=request.POST['email']
        password=request.POST['password']
        print(email)
        user=authenticate(email=email,password=password)
        user_details=Myuser.objects.get(email=email)
        user_type=user_details.user_type
        
        if user is not None:
            if user.is_active:
                login(request,user)
                if user_type=="HSP" :
                    #return HttpResponse("<html>Welcome to Ambulance</html>")
                    return redirect('Hospital:index')
                    
                elif user_type=="AMB" :
                    #return HttpResponse("<html>Welcome to Ambulance</html>")
                    return redirect('Ambulance:index')

                elif user_type=="BLB" :
                    #return HttpResponse("<html>Welcome to BLoodBank</html>")
                    return redirect('bloodbank:index')
                elif user_type=="MST":
                    return redirect('Medical_Store:index')

                    #return HttpResponse("<html>Welcome to Medical Store</html>")
                    #return redirect('Attendance_manager:index_student')
                else :
                    return HttpResponse("</html>Not Selected valid user type</html>")
                   # return redirect('Attendance_manager:mark_attendance')
                #messages.info(request, 'Your have successfully loged in!')
                #return redirect('myuser:login')
            else:
                return render(request, 'myuser/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'myuser/login.html', {'form':form,'error_message': 'Invalid login'})
        return render(request,self.template_name,{'form':form})

class LogoutView(View):
    form_class=LoginForm
    template_name='myuser/login.html'
    def get(self,request):
        form=self.form_class(None)
        logout(request)
        return redirect(reverse('myuser:login'))

class Delete(DeleteView):
    model=Myuser
    success_url=reverse_lazy('myuser:login')

