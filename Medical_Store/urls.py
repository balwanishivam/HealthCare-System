from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="mdstore"

urlpatterns=[
    # path('/report/',views.reports,name="report"),
    # path('search/',views.search,name="search"),
    # path('serach/city/<slug:city>/',views.city_search,name="city_search"),
    # path('search/bloodgroup/<slug:bloodgroup>/',views.bloodgroup_search,name='bloodgroup_search'),
    # path('admin/',views.admin,name='admin'),
    # path('admin/add_blood',views.add_blood,name='add_blood'),
    # path('admin/add_reciever',views.add_reciever,name='add_reciever'),
    # path('admin/add_donor',views.add_donor,name='add_donor'),
    # path('admin/edit_blood',views.edit_blood,name='edit_blood'),
    # path('admin/edit_reciever',views.edit_reciever,name='edit_reciever'),
    # path('admin/edit_donor',views.edit_donor,name='edit_donor'),
    
]
