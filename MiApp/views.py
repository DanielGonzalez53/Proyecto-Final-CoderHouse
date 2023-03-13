from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Producto
from .forms import UserRegisterForm, ProductoForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

@login_required
def inicio(request):
    return render(request, 'MiApp/inicio.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'registration/login.html', {'mensaje': 'Usuario Creado '})
    else:
        form = UserRegisterForm()

    return render(request, 'MiApp/registro.html', {'form':form})

def about(request):
    return render(request, 'MiApp/about.html')

def quieroVender(request):
    return render(request, 'MiApp/quieroVender.html')

'''
def quieroVender(request):
    data = {
        'miProducto': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Entregable registrado con exito.'
            return render(request, "MiApp/inicio.html")
        else:
            data['miProducto'] = formulario
    return render(request, 'MiApp/quieroVender.html', data)
'''

class ProductoList(ListView):
    model = Producto
    template_name = 'MiApp/producto_list.html'

class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'MiApp/producto_detalle.html'

'''
class ProductoCreacion(CreateView, SuccessMessageMixin):
    model = Producto
    form = ProductoForm
    fields = ['tipo', 'nombre', 'marca', 'imagen', 'descripcion', 'precio', 'activo']
    template_name = 'MiApp/quieroVender.html'
    success_message = 'Producto creado exitosamente!'

    def get_success_url(self):
        return reverse('Inicio')
'''
        
class ProductoCreacion(CreateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('Inicio')
    template_name = 'MiApp/quieroVender.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductoCreacion, self).form_valid(form)

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = 'MiApp/quieroVender/list'
    fields = '__all__'

class ProductoDelete(DeleteView):
    model = Producto
    success_url = 'MiApp/quieroVender/list'