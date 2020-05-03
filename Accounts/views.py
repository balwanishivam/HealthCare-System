from django.views.generic import *
from django.views.generic.edit import *
from .models import *
from django.urls import reverse_lazy,reverse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

class UserFormView(View):
    form_class=UserForm
    template_name='Accounts/registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('Accounts:login')
        
        return render(request,self.template_name,{'form':form})

class LoginView(View):
    form_class=LoginForm
    template_name='Accounts/login.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        Login_type=request.POST['Login_type']
        user=authenticate(username=username,password=password)
        #Login_type=UserProfile.objects.get(id=self.request.user.id)
        if user is not None:
            if user.is_active:
                login(request,user)
                if Login_type=="HSP":
                    return HttpResponseRedirect("Welcome to Hospital")
                    #return redirect('Attendance_manager:index_student')
                elif Login_type=="AMB":
                    return HttpResponseRedirect("Welcome to Ambulance")
                    #return redirect('Attendance_manager:index_student')
                elif Login_type=="BLB":
                    return HttpResponseRedirect("Welcome to BLoodBank")
                    #return redirect('Attendance_manager:index_student')
                elif Login_type=="MST":
                    return HttpResponseRedirect("Welcome to MEdical Store")
                    #return redirect('Attendance_manager:index_student')
                else :
                    return HttpResponseRedirect("Not Selected valid user type")
                   # return redirect('Attendance_manager:mark_attendance')
                #messages.info(request, 'Your have successfully loged in!')
                #return redirect('Accounts:login')
            else:
                return render(request, 'Accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Accounts/login.html', {'form':form,'error_message': 'Invalid login'})
        return render(request,self.template_name,{'form':form})

class LogoutView(View):
    form_class=LoginForm
    template_name='Accounts/login.html'
    def get(self,request):
        form=self.form_class(None)
        logout(request)
        return redirect(reverse('Accounts:login_user'))

