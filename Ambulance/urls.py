from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
app_name="Ambulance"

urlpatterns=[
    path('',views.Index.as_view(),name="index"),
    path('register/',views.UserCreate.as_view(),name="register"),
    # Ambulance Servicce
    path('add_ambulance/',views.AddAmbulance.as_view(),name="add_ambulance"),
    path('<int:pk>/edit_ambulance/',views.EditAmbulance.as_view(),name="edit_ambulance"),
    path('<int:pk>/delete_ambulance/',views.DeleteAmbulance.as_view(),name="delete_ambulance"),
    path('view_ambulance/',views.ViewAmbulance.as_view(),name="view_ambulance"),
    # path('/report/',views.reports,name="report"),
    # path('search/',views.search,name="search"),
    # path('search/pincode/<slug:pincode>/',views.pincode_search,name="pincode_search"),
    # path('admin/',views.admin,name='admin'),
    # path('admin/edit_ambulance',views.edit_ambulance,name='edit_ambulance'),
    # path('admin/delete_ambulance',views.delete_ambulance,name='delete_ambulance'),
    # path('admin/provider_detail',views.provider_detail,name='provider_detail'),

]
