from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="myuser"

urlpatterns=[
    # path('',views.index,name='index'),
    path('',views.Index.as_view(),name="index"),
    path('search_ambulance',views.SearchAmbulance.as_view(),name="search_ambulance"),
    path('<int:pincode>/view_ambulance',views.ViewAmbulance.as_view(),name="view_ambulance"),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('<pk>/delete',views.Delete.as_view(),name='delete'),
    path('logout/',views.LogoutView.as_view(),name='logout')
    # path('forgotpassword/',views.forgotpassword,name='forgotpasssword')
]
