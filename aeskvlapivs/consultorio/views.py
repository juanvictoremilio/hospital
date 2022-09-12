from unicodedata import name
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from . import models
from django.db.models import Q
from .models import Paciente, Urgencias
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Paciente, Reevaluacion
from .forms import PacienteForm, ReevaluacionForm, UrgenciasForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

def uploadFilePac(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["Imagenología1", 'Imagnología2', 'Imagenología3','Labs1', 
        'Labs2', 'Labs3']

        # Saving the information in the database
        document = models.Paciente(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Paciente.objects.all()

    return render(request, "consultorio/paciente_list.html", context = {
        "paciente": documents
    })


class SearchResultsView(ListView):
    model = Paciente
    template_name = 'search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Paciente.objects.filter(
            Q(name__icontains=query) | Q(phone__icontains=query)
        )
        return object_list

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente_list.html'
    
    

class PacienteDetailView(DetailView):
    model = Paciente

    
@method_decorator(staff_member_required, name='dispatch')
class PacienteCreate(CreateView):
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('consultorio:pacientes')


@method_decorator(staff_member_required, name='dispatch')
class PacienteUpdate(UpdateView):
    model = Paciente
    form_class = PacienteForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        return reverse_lazy('consultorio:actualizar_paciente', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PacienteDeleteView(DeleteView):
    model = Paciente
    success_url = reverse_lazy('consultorio:pacientes')






# Create your views here.


#def pacientes(request):
 #   pacientes = get_list_or_404(Paciente)
  #  return render(request, 'consultorio/pacientes.html', {'pacientes':pacientes})

#def paciente(request, page_id, page_slug):
 #   paciente = get_object_or_404(Paciente, id=page_id)
  #  return render(request, 'consultorio/paciente.html', {'paciente':paciente})



#REEVALUACION


def uploadFileReev(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["Imagenología1", 'Imagnología2', 'Imagenología3','Labs1', 
        'Labs2', 'Labs3']

        # Saving the information in the database
        document = models.Reevaluacion(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Reevaluacion.objects.all()

    return render(request, "consultorio/reevaluacion_list.html", context = {
        "reevaluacion": documents
    })


class SearchReevResultsView(ListView):
    model = Reevaluacion
    template_name = 'searchreev_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Reevaluacion.objects.filter(
            Q(paciente__name__icontains=query)
        )
        return object_list



class ReevaluacionListView(ListView):
    model = Reevaluacion
    template_name = 'reevaluacion_list.html'
    
    

class ReevalucionDetailView(DetailView):
    model = Reevaluacion


@method_decorator(staff_member_required, name='dispatch')
class ReevaluacionCreate(CreateView):
    model = Reevaluacion
    form_class = ReevaluacionForm
    success_url = reverse_lazy('consultorio:reevaluaciones')


@method_decorator(staff_member_required, name='dispatch')
class ReevaluacionUpdate(UpdateView):
    model = Reevaluacion
    form_class = ReevaluacionForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        return reverse_lazy('consultorio:Actualizar_reevaluacion', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class ReevalucionDeleteView(DeleteView):
    model = Reevaluacion
    success_url = reverse_lazy('consultorio:reevaluaciones')



#URGENCIAS

def uploadFileUrgencias(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["Imagenología1", 'Imagnología2', 'Imagenología3','Labs1', 
        'Labs2', 'Labs3']

        # Saving the information in the database
        document = models.Urgencias(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Urgencias.objects.all()

    return render(request, "consultorio/urgencias_list.html", context = {
        "urgencias": documents
    })


class SearchUrgenciasResultsView(ListView):
    model = Urgencias
    template_name = 'searchurg_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Urgencias.objects.filter(
            Q(nombre__name__icontains=query)
        )
        return object_list



class UrgenciasListView(ListView):
    model = Urgencias
    template_name = 'urgencias_list.html'
    
    

class UrgenciasDetailView(DetailView):
    model = Urgencias


@method_decorator(staff_member_required, name='dispatch')
class UrgenciasCreate(CreateView):
    model = Urgencias
    form_class = UrgenciasForm
    success_url = reverse_lazy('consultorio:pacientes_urgencias')



@method_decorator(staff_member_required, name='dispatch')
class UrgenciasUpdate(UpdateView):
    model = Urgencias
    form_class = UrgenciasForm
    template_name_suffix = '_update_form'

    
    def get_success_url(self):
        return reverse_lazy('consultorio:actualizar_urgencia', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class UrgenciasDeleteView(DeleteView):
    model = Urgencias
    success_url = reverse_lazy('consultorio:pacientes_urgencias')







