from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
app_name="Hospital"

urlpatterns=[
    path('register/',views.UserCreate.as_view(),name="register"),
    path('',views.Index.as_view(),name="index"),

    #Doctor Url
    path('view_doctor/',views.ViewDoctor.as_view(),name="view_doctor"),
    path('add_doctor',views.AddDoctor.as_view(),name='add_doctor'),
    path('<int:pk>/delete_doctor',views.DeleteDoctor.as_view(),name='delete_doctor'),
    path('<int:pk>/edit_doctor',views.EditDoctor.as_view(),name='edit_doctor'),

    #Patient Url
    path('view_patient/',views.ViewPatient.as_view(),name="view_patient"),
    path('add_patient',views.AddPatient.as_view(),name='add_patient'),
    path('<int:pk>/delete_patient',views.DeletePatient.as_view(),name='delete_patient'),
    path('<int:pk>/edit_patient',views.EditPatient.as_view(),name='edit_patient'),
   
    #Test Url
    path('view_test/',views.ViewTest.as_view(),name="view_test"),
    path('add_test',views.AddTest.as_view(),name='add_test'),
    path('<int:pk>/delete_test',views.DeleteTest.as_view(),name='delete_test'),
    path('<int:pk>/edit_test',views.EditTest.as_view(),name='edit_test'),

    #Conducted Url
    path('view_conducted/',views.ViewConducted.as_view(),name="view_conducted"),
    path('add_conducted',views.AddConducted.as_view(),name='add_conducted'),
    path('<int:pk>/delete_conducted',views.DeleteConducted.as_view(),name='delete_conducted'),
    path('<int:pk>/edit_conducted',views.EditConducted.as_view(),name='edit_conducted'),
    
]
