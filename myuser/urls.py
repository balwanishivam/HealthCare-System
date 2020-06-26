from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="myuser"

urlpatterns=[
    # path('',views.index,name='index'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('search_ambulance', views.SearchAmbulance.as_view(),name='search_ambulance'),
    path('<int:pincode>/view_ambulance', views.ViewAmbulance.as_view(),name='view_ambulance'),
    path('search_hospital', views.SearchHospital.as_view(),name='search_hospital'),
    path('<int:pincode>/view_hospital', views.ViewHospital.as_view(),name='view_hospital'),
    path('search_bloodbank', views.ViewBloodbank.as_view(),name='search_bloodbank'),
    path('<int:pincode>/view_bloodbank', views.ViewBloodbank.as_view(),name='view_bloodbank'),
    path('search_medicine', views.SearchMedicine.as_view(),name='search_medicine'),
    path('<int:pincode>/view_medicine', views.ViewMedicine.as_view(),name='view_medicine'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('<pk>/delete',views.Delete.as_view(),name='delete'),
    path('logout/',views.LogoutView.as_view(),name='logout')
    # path('forgotpassword/',views.forgotpassword,name='forgotpasssword')
]
