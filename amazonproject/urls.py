"""amazonproject URL Configuration

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
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amazon/', views.home),
    path('amazon1/', views.amazon),
    path('history/', views.history),
    path('about/', views.about),
    path('feedback/', views.feedback),
    path('products/',views.products),
    path('second/',views.second),
    path('third/',views.third),
    path('fourth/',views.fourth),
    path('tshirt/',views.buyt),
    path('logout/',views.logout),
    path('mobiles/',views.mobile),
    path('laptops/',views.laptop),
    path('vehicles/',views.vehicle),
    path('clothes/',views.clothes),
    path('earphones/',views.earphone),
    path('shoes/',views.shoes),
    path('football/',views.football),
    path('volleyball/',views.volleyball),
    path('cricket/',views.cricket),
    path('tennis/',views.tennis),
    path('toys/',views.toys),
    path('shirts/',views.shirts)


]
