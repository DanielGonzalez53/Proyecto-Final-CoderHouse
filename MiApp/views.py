from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

@login_required
def about(request):
    return render(request, 'MiApp/about.html')

class ProductoList(ListView):
    model = Producto
    template_name = 'MiApp/producto_list.html'

class ProductoDetalle(DetailView):
    model = Producto
    template_name = 'MiApp/producto_detalle.html'
   
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
    success_url = reverse_lazy('List')
    fields = '__all__'

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('List')

#TECNOLOGIA

class TecnologiaLista(ListView):
    context_object_name = 'tecnologias'
    queryset = Producto.objects.filter(tipo__startswith='tecnologia')
    template_name = 'MiApp/tecnologiaLista.html'

class TecnologiaDetalle(DetailView):
    model = Producto
    context_object_name = 'tecnologia'
    template_name = 'MiApp/tecnologiaDetalle.html'

class TecnologiaUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('tecnologias')
    context_object_name = 'tecnologia'
    template_name = 'MiApp/tecnologiaEdicion.html'

class TecnologiaDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('tecnologias')
    context_object_name = 'tecnologia'
    template_name = 'MiApp/tecnologiaBorrado.html'

#DEPORTES

class DeporteLista(ListView):
    context_object_name = 'deportes'
    queryset = Producto.objects.filter(tipo__startswith='deporte')
    template_name = 'MiApp/deporteLista.html'

class DeporteDetalle(DetailView):
    model = Producto
    context_object_name = 'deporte'
    template_name = 'MiApp/deporteDetalle.html'

class DeporteUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('deportes')
    context_object_name = 'deporte'
    template_name = 'MiApp/deporteEdicion.html'

class DeporteDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('deportes')
    context_object_name = 'deporte'
    template_name = 'MiApp/deporteBorrado.html'

#VEHICULOS

class VehiculoLista(ListView):
    context_object_name = 'vehiculos'
    queryset = Producto.objects.filter(tipo__startswith='vehiculo')
    template_name = 'MiApp/vehiculoLista.html'

class VehiculoDetalle(DetailView):
    model = Producto
    context_object_name = 'vehiculo'
    template_name = 'MiApp/vehiculoDetalle.html'

class VehiculoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('vehiculos')
    context_object_name = 'vehiculo'
    template_name = 'MiApp/vehiculoEdicion.html'

class VehiculoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('vehiculos')
    context_object_name = 'vehiculo'
    template_name = 'MiApp/vehiculoBorrado.html'

