from django.urls import path
from . import views

app_name="Medical_Store"

urlpatterns=[
    path('register/',views.UserCreate.as_view(),name="register"),
    path('add_company/',views.AddCompany.as_view(),name="add_company"),
    path('add_medicine/',views.AddMedicine.as_view(),name="add_medicine"),
    # path('/report/',views.reports,name="report"),
    # path('search/',views.search,name="search"),
    # path('serach/city/<slug:city>/',views.city_search,name="city_search"),
    # path('search/pincode/<int:pincode>/',views.pincode_search,name='pincode_search'),
    # path('search/medicine/<slug:medicine>/',views.medicine_search,name='medicine_search'),    
    # path('admin/',views.admin,name='admin'),
    # path('admin/add_medicine',views.add_medicine,name='add_medicine'),
    # path('admin/edit_medicine',views.edit_medicine,name='edit_medicine'),
    # path('admin/delete_medicine',views.delete_medicine,name='delete_medicine'),
    # path('admin/add_company',views.add_company,name='add_company'),
    # path('admin/edit_company',views.edit_company,name='edit_company'),
    # path('admin/delete_company',views.delete_company,name='delete_company'),
    # path('admin/store_details',views.store_details,name='store_details'),    
]
