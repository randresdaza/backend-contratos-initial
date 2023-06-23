"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from authApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from django.urls import path

urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('userCreate/',views.UserCreateView.as_view()),
    path('users/',views.UserView.as_view()),
    path('users/<int:pk>/', views.UserView.as_view()),
    path('users/username/<str:username>/', views.UserView.as_view()),
    path('roles/',views.RolView.as_view()),
    path('roles/<int:pk>/', views.RolView.as_view()),
    path('dependencias/',views.DependenciaView.as_view()),
    path('dependencias/<int:pk>/',views.DependenciaView.as_view()),
    path('series/',views.SerieView.as_view()),
    path('series/<int:pk>/',views.SerieView.as_view()),
    path('subSeries/',views.SubSerieView.as_view()),
    path('subSeries/<int:pk>/', views.SubSerieView.as_view()),
]