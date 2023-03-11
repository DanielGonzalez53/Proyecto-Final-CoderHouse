from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'MiApp/inicio.html')

def about(request):
    return render(request, 'MiApp/about.html')

@login_required
def quieroVender(request):
    return render(request, 'MiApp/quieroVender.html')