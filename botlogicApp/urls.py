from django.contrib import admin
from django.urls import path
from .import views
from .views import error

urlpatterns = [

    path('', views.botmain, name="botymain"),
    path('error', error, name="error"),


]
