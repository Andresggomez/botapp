from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name="Inicio"),

    path('tienda/', include('tiendaApp.urls')),
    path('bot/', include('botlogicApp.urls')),
    path('error/', include('botlogicApp.urls')),
    path('nuevoUsuario/', include('freemiumApp.urls')),
    path('entrar/', include('freemiumApp.urls')),
    path('datosbtc1d/', include('botybtc1mApp.urls')),
    path('cripto/', include('criptoApp.urls')),

    path('carro/', include('carro.urls')),

    path('contacto/', views.contacto, name="Contacto"),
    path('noticias/', views.noticias, name="Noticias"),
    path('registro/', views.registro, name="Registro"),
    path('servicios/', views.servicios, name="Servicios"),


]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
