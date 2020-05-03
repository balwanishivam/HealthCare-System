from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="Hospital"

urlpatterns=[
    # path('/report/',views.reports,name="report"),
    # path('search/',views.search,name="search"),
    # path('serach/city/<slug:city>/',views.city_search,name="city_search"),
    # path('search/doctor/<slug:doctor>/',views.doctor_search,name='doctor_search'),
    # path('admin/',views.admin,name='admin'),
    # path('admin/add_patient_record',views.add_patient_record,name='add_patient_record'),
    # path('admin/add_doctor',views.add_doctor,name='add_doctor'),
    # path('admin/add_tests',views.add_tests,name='add_tests'),
    # path('admin/add_conducted',views.add_conducted,name='add_conducted'),
    
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
