from django.shortcuts import render

def inicio(request):
    return render(request, 'MiApp/inicio.html')

def acercaDeMi(request):
    return render(request, 'MiApp/acercaDeMi.html')