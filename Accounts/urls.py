from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name="accounts"

urlpatterns=[
    # path('',views.index,name='index'),
    # path('login/',views.login,name='login'),
    # path('register/',views.register,name='register'),
    # path('forgotpassword/',views.forgotpassword,name='forgotpasssword')
]
