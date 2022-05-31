from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    API_KEY=models.CharField(max_length=65)
    API_SECRET_KEY=models.CharField(max_length=65)
    protecionDatos=models.BooleanField()
    avisoTelegram=models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def __str__(self):
        return self.nombre