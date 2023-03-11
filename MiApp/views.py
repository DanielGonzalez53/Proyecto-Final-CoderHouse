from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Productos, Categoria
from django.contrib import messages
from .forms import UserRegisterForm

@login_required
def inicio(request):
    categorias=Categoria.objects.filter(activo=True)
    productos=Productos.objects.filter(activo=True)
    return render(request, 'MiApp/inicio.html', {'productos':productos,'categorias':categorias})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'MiApp/inicio.html', {'mensaje': 'Usuario Creado '})

    else:
        form = UserRegisterForm()

    return render(request, 'MiApp/registro.html', {'form':form})

'''def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
        else:
            form = UserCreationForm()
    return render(request, 'MiApp/register.html', {'form':form})'''

def buscar_categorias(request, slug):
    cat = Categoria.objects.get(slug=slug)
    categorias = Categoria.objects.filter(activo=True)
    productos = Productos.objects.filter(activo=True, categoria=cat)
    return render(request, 'MiApp/list.html', {'productos':productos,'categorias':categorias})

def search(request):
    template_name = 'MiApp/list.html'
    q = request.GET['q']
    productos = Productos.objects.filter(activo=True,nombre__icontains=q)
    categorias = Categoria.objects.filter(activo=True)
    return render(request, template_name, {'productos':productos,'categorias':categorias})

def about(request):
    return render(request, 'MiApp/about.html')

def quieroVender(request):
    return render(request, 'MiApp/quieroVender.html')