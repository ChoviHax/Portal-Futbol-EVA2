from django.contrib import admin
from .models import Jugador, Equipo


@admin.register(Jugador)
class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'nacionalidad', 'equipo')
    search_fields = ('nombre', 'posicion', 'nacionalidad', 'equipo__nombre')
    list_filter = ('posicion', 'nacionalidad', 'equipo')


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')