from django.db import models

class Foto(models.Model):

    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="album")

    def __unicode__(self):
        return self.titulo