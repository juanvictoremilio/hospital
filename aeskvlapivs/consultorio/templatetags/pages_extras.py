from django import template
from consultorio.models import Paciente

register = template.Library()

@register.simple_tag
def get_paciente_list():
    pacientes = Paciente.objects.all()
    return pacientes