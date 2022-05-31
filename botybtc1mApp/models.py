from django.db import models

# Create your models here.

class btc1m(models.Model):
    cripto = models.CharField(max_length=10)
    rsi = models.IntegerField()
    estado = models.CharField(max_length=10)
    tendencia = models.CharField(max_length=10)
    precio = models.IntegerField()
    recomendacion = models.CharField(max_length=10)
    posicionCorta = models.IntegerField()
    posicionLarga = models.IntegerField()

    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'cripto'
        verbose_name_plural = 'criptos'

    def __str__(self):
        return self.titulo
