"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import Dashboard,Loginview,pm, signupview,Noti,Addmedicine,Addpatient,Dmedicine,Hospital,Medicine,Patientlist,Payment,Search,Share,addmedicineview

urlpatterns = [


    # path('',hello),
    path('',pm),
    path('login/',Loginview,name='login'),
    path('signup/',signupview,name='signup'),
    path('dashboard/',Dashboard,name='dashboard'),
    path('noti/',Noti,name='noti'),
    path('addmedicine/',addmedicineview,name='addmedicine'),
    path('addpatient/',Addpatient,name='addpatient'),
    path('dmedicine/',Dmedicine,name='dmedicine'),
    path('hospital/',Hospital,name='hospital'),
    path('medicine/',Medicine,name='medicine'),
    path('patientlist/',Patientlist,name='patientlist'),
    path('payment/',Payment,name='payment'),
    path('search/',Search,name='search'),
    path('share/',Share,name='share'),

]
