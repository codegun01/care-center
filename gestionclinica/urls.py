"""
URL configuration for gestionclinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('patients/', views.patients, name='patients'),
    #path('create/patients/', views.createPatient, name='create_patient'),
    path('create/', views.createPatient, name='create_patient'),
    #path('patients/<int:id>/', views.patient_detail, name='patient_detail'),
    path('/<int:id>', views.patient_detail, name='patient_detail'),
    #path('patient_detail/', views.patient_detail, name='patient_detail'),
    path('signout', views.signout, name='signout'),
    path('patients/<int:patient_id>', views.edit_patient, name='edit_patient'),
    path('patients/<int:patient_id>/delete', views.delete_patient, name='delete_patient')
]
