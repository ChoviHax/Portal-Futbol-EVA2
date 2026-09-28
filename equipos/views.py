from django.shortcuts import render
from futbol.models import Equipo


def equipos(request):
    lista_equipos = Equipo.objects.all()

    contexto = {
        'equipos': lista_equipos
    }

    return render(request, 'equipos/equipos.html', contexto)