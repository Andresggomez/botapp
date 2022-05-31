from django.contrib import admin
from .models import Noticia

# Register your models here.
# Configurar lo que se ve en admin

class Noticia_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Noticia, Noticia_Admin)
