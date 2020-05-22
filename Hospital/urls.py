from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
app_name="Hospital"

urlpatterns=[
    path('register/',views.UserCreate.as_view(),name="register"),
    path('',views.Index.as_view(),name="index"),
    path('add_patient_record',views.AddPatient.as_view(),name='add_patient_record'),
    path('add_doctor',views.AddDoctor.as_view(),name='add_doctor'),
    path('add_test',views.AddTest.as_view(),name='add_test'),
    path('add_conducted',views.PatientTest.as_view(),name='add_conducted'),
    
    # path('/report/',views.reports,name="report"),
    # path('search/',views.search,name="search"),
    # path('serach/city/<slug:city>/',views.city_search,name="city_search"),
    # path('search/doctor/<slug:doctor>/',views.doctor_search,name='doctor_search'),
    # path('admin/',views.admin,name='admin'),
    # EDIT ALL THESE DETAILS 
    # path('admin/add_patient_record',views.add_patient_record,name='add_patient_record'),
    # path('admin/add_doctor',views.add_doctor,name='add_doctor'),
    # path('admin/add_tests',views.add_tests,name='add_tests'),
    # path('admin/add_conducted',views.add_conducted,name='add_conducted'),
    
    # DELETE THESE RECORDS
    # path('admin/add_patient_record',views.add_patient_record,name='add_patient_record'),
    # path('admin/add_doctor',views.add_doctor,name='add_doctor'),
    # path('admin/add_tests',views.add_tests,name='add_tests'),
    # path('admin/add_conducted',views.add_conducted,name='add_conducted'),
]
