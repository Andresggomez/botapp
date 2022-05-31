from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.botybtc1m, name="botybtc1m"),


]
