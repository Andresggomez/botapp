from django.contrib import admin
from .models import Usuario

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = (('created', 'updated', 'API_KEY', 'API_SECRET_KEY', 'protecionDatos' ))

admin.site.register(Usuario, UsuarioAdmin)
