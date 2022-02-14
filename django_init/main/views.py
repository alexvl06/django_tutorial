from django.shortcuts import render
from .models import persona

def inicio(request):
    personas = persona.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request, "index.html", contexto) 