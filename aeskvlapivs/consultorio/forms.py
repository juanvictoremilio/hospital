from logging import PlaceHolder
from django import forms
from .models import Paciente, Reevaluacion, Urgencias
from django import forms

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['name', 'gender', 'dob', 'nationality', 'etnia', 'scholarship', 'job',
     'religion', 'sport', 'civil_status', 'adress', 'email', 'phone', 'entitlement', 'specify',
     'insurance', 'immediate_background', 'smoking', 'alcohol', 'drugs_adictions', 'allergies',
     'dislipidemia', 'dm', 'hta', 'inf_ang_de_pecho', 'evc', 'ivp', 'EPOC', 'cancer', 'otras_enf',
     'cir_previas', 'obs', 'actual_situation', 'tension_sistolica', 'tension_diastolica', 'fc','fr',
     'temp', 'saturacion', 'dextrostix', 'a1c', 'peso', 'estatura', 'per_abdominal', 'Imagenología1',
     'Imagenología2', 'Imagenología3', 'Labs1', 'Labs2', 'recetas', 'diagnosis', 'obs', 'txs',
     'adendums', 

    ]
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}, ),
            
            'dob': forms.DateInput( attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'}),
            
            'nationality': forms.TextInput(attrs={'class':'form-control'}),
            'etnia': forms.TextInput(attrs={'class':'form-control'}),
            'scholarship': forms.TextInput(attrs={'class':'form-control'}),
            'job': forms.TextInput(attrs={'class':'form-control'}),
            'adress': forms.TextInput(attrs={'class':'form-control'}),
            'immediate_background': forms.Textarea(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control'}),
            'cir_previas': forms.TextInput(attrs={'class':'form-control'}),
            'otras_enf': forms.Textarea(attrs={'class':'form-control'}),
            'actual_situation': forms.Textarea(attrs={'class':'form-control'}),
          
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'txs': forms.Textarea(attrs={'class':'form-control'}),
            'adendums': forms.Textarea(attrs={'class':'form-control'}),
                        
        }


class ReevaluacionForm(forms.ModelForm):
    class Meta:
        model = Reevaluacion
        fields = ['paciente', 'age', 'dxs_previos', 'immediate_background',
        'tension_sistolica', 'tension_diastolica', 'fc', 'fr', 'temp', 'saturacion', 'dextrostix', 'a1c', 'peso', 'estatura',
        'per_abdominal', 'expl', 'Imagenología1', 'Imagenología2', 'Imagenología3', 'Labs1', 'Labs2',
        'recetas', 'diagnosis', 'obs', 'txs', 

    ]
        raw_id_fields = ('paciente', )
        autocomplete_fields = ('paciente',)
        widgets = {
            'immediate_background': forms.Textarea(attrs={'class':'form-control'}),
            'expl': forms.Textarea(attrs={'class':'form-control'}),
            'dxs_previos': forms.Textarea(attrs={'class':'form-control'}),
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'obs': forms.Textarea(attrs={'class':'form-control'}),
            'txs': forms.Textarea(attrs={'class':'form-control'}),
            
                       
        }
        

class UrgenciasForm(forms.ModelForm):
    class Meta:
        model = Urgencias
        fields = ['nombre', 'edad', 'im_bkground', 'other_bkground', 'fr', 'O2', 'saturacion', 'fc', 'tension_sistolica', 'tension_diastolica', 'Diaforesis',
        'AVPU', 'apertura_ocular', 'Respuesta_Verbal', 'Respuesta_Motora', 'dextrostix', 'temp', 'peso', 'estatura', 'per_abdominal',
         'expl', 'dxs', 'MANEJO_INICIAL', 'OBSERVACIONES_GENERALES' ]

        raw_id_fields = ('nombre', )
        autocomplete_fields = ('nombre',)
        widgets = {
                   
            'im_bkground': forms.Textarea(attrs={'class':'form-control', 
            'placeholder':'Describa por qué llegó el paciente, quien lo trajo o como llegó, qué sucedió antes (se desmayó, tuvo un accidente. empezó a sentirse mal...), describa el habitus exterior y los síntomas que el paciente pueda referir'}),
            'other_bkground': forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Describa y recopile enfermedades previas, alergias y lo que considere importante'}),
            'expl': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Complemente el hábitus exterior y escriba lo relevante desde la cabeza a los pies'}),
            'dxs': forms.Textarea(attrs={'class':'form-control'}),
            'MANEJO_INICIAL': forms.Textarea(attrs={'class':'form-control'}),
            'immediate_background': forms.Textarea(attrs={'class':'form-control'}),
            'OBSERVACIONES_GENERALES': forms.Textarea(attrs={'class':'form-control'}),
         
                        
        }