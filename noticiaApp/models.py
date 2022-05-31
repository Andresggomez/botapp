from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=700)
    imagen=models.ImageField(upload_to='noticias')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='noticia'
        verbose_name_plural='noticias'

    def __str__(self):
        return self.titulo
