from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Tecnologia
from django.contrib import messages
from .forms import UserRegisterForm, TecnologiaFormulario
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

class TecnologiaCrear(CreateView):
    model = Tecnologia
    form_class = TecnologiaFormulario
    success_url = reverse_lazy('Inicio')
    template_name = 'MiApp/tecnologiaCrear.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TecnologiaCrear, self).form_valid(form)
    
class TecnologiaLista(ListView):
    model = Tecnologia
    context_object_name = 'tecnologias'
    queryset = Tecnologia.objects.all()
    template_name = 'MiApp/tecnologiaLista.html'
