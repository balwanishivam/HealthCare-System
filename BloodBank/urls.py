from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="bloodbank"

urlpatterns=[
    path('register/',views.UserCreate.as_view(),name="register"),
    path('',views.Index.as_view(),name="index"),

    #Donor Url
    path('view_donor',views.ViewDonor.as_view(),name="view_donor"),
    path('add_donor',views.AddDonor.as_view(),name='add_donor'),
    path('<int:pk>/delete_donor',views.DeleteDonor.as_view(),name='delete_donor'),
    path('<int:pk>/edit_donor',views.EditDonor.as_view(),name='edit_donor'),

    #Reciever Url
    path('view_receiver',views.ViewReceiver.as_view(),name="view_receiver"),
    path('add_receiver',views.AddReceiver.as_view(),name='add_receiver'),
    path('<int:pk>/delete_receiver',views.DeleteReceiver.as_view(),name='delete_receiver'),
    path('<int:pk>/edit_receiver',views.EditReceiver.as_view(),name='edit_receiver'),
    
    #Inventory Url
    path('view_inventory',views.ViewInventory.as_view(),name="view_inventory"),
    path('add_reviever',views.AddInventory.as_view(),name='add_inventory'),
    path('<int:pk>/delete_inventory',views.DeleteInventory.as_view(),name='delete_inventory'),
    path('<int:pk>/edit_inventory',views.EditInventory.as_view(),name='edit_inventory'),

]
