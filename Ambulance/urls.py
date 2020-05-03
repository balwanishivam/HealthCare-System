from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="Ambulance"

urlpatterns=[
    # path('/report/',views.reports,name="report"),
    # path('search/',views.search,name="search"),
    # path('serach/pincode/<slug:pincode>/',views.pincode_search,name="pincode_search"),
    # path('admin/',views.admin,name='admin'),
    # path('admin/add_ambulance',views.add_ambulance,name='add_ambulance'),
    # path('admin/edit_ambulance',views.edit_ambulance,name='edit_ambulance'),
    # path('admin/delete_ambulance',views.delete_ambulance,name='delete_ambulance'),
    # path('admin/provider_detail',views.provider_detail,name='provider_detail'),

]
