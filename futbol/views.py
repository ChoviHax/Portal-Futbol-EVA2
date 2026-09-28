from django.shortcuts import render
from .models import Jugador


def inicio(request):
    return render(request, 'futbol/inicio.html')


def jugadores(request):
    lista_jugadores = Jugador.objects.all()

    contexto = {
        'jugadores': lista_jugadores
    }

    return render(request, 'futbol/jugadores.html', contexto)