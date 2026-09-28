from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    equipo = models.ForeignKey(
    Equipo,
    on_delete=models.CASCADE,
    related_name='jugadores'
)
    imagen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre