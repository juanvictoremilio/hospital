
from tkinter import Text
from unicodedata import name
from django.contrib import admin
from django.forms import TextInput
from .models import Paciente, Reevaluacion, Urgencias
from django import forms

# Register your models here.

admin.site.site_header = "Expediente Clínico AESKVLAPIVS "
admin.site.site_title = "AESKVLAPIVS"
admin.site.index_title = "Bienvenido a tu escritorio médico"


class PacienteAdmin(admin.ModelAdmin):
	list_display = ['name', 'age', 'phone', 'email','diagnosis','dextrostix', 'a1c', 'imc', 'climc','timestamp', 'update']
	readonly_fields = ('timestamp', 'update')
	search_fields = ('name', 'phone', 'email')
	list_filter = ['entitlement']


class ReevaluacionAdmin(admin.ModelAdmin):
	list_display=['paciente', 'age', 'phone', 'email', 'dextrostix', 'a1c', 'imc', 'climc', 'per_abdominal', 
	'immediate_background', 'timestamp', 'reevaluación']
	readonly_fields = ('timestamp', 'update')
	list_filter = ['timestamp', 'entitlement']
	search_fields = ('paciente__name', 'phone', 'email')
	autocomplete_fields = ('paciente',)


class UrgenciasAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'dxs', 'NEUROLOGICO', 'RESPIRATORIO', 'HEMODINAMICO']
	autocomplete_fields = ('nombre',)
	readonly_fields = ('timestamp', 'update')
	search_fields = ('paciente__name',)

class Media:
        css = {
            'all': ('consultorio/css/custom_ckeditor.css',)
		}
	


admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Reevaluacion, ReevaluacionAdmin)
admin.site.register(Urgencias, UrgenciasAdmin)






