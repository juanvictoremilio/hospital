from logging import PlaceHolder
from django import forms
from .models import Paciente, Reevaluacion, Urgencias, Urgencias_Reevaluaciones

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['name', 'gender', 'dob', 'nationality', 'etnia', 'scholarship', 'job',
     'religion', 'sport', 'civil_status', 'adress', 'email', 'phone', 'entitlement', 'specify',
     'insurance', 'immediate_background', 'smoking', 'alcohol', 'drugs_adictions', 'allergies',
     'dislipidemia', 'dm', 'hta', 'inf_ang_de_pecho', 'evc', 'ivp', 'athma', 'EPOC', 'cancer', 'blood_type', 'otras_enf',
     'Menarca', 'FUR', 'Gestas', 'Partos', 'Cesareas', 'pap', 'mast', 'obsgin', 'medications_list',
     'cir_previas', 'obs', 'actual_situation', 'tension_sistolica', 'tension_diastolica', 'fc','fr',
     'temp', 'saturacion', 'dextrostix', 'a1c', 'peso', 'estatura', 'per_abdominal', 'Doc1',
     'Doc2', 'Doc3', 'Doc4', 'Doc5', 'recetas', 'diagnosis', 'obs', 'txs', 'especialidad',
     'esp_otro', 'adendums',

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
            'obsgin': forms.Textarea(attrs={'class':'form-control'}),
            'otras_enf': forms.Textarea(attrs={'class':'form-control'}),
            'medications_list': forms.Textarea(attrs={'class':'form-control'}),
            'actual_situation': forms.Textarea(attrs={'class':'form-control'}),
          
            'diagnosis': forms.Textarea(attrs={'class':'form-control'}),
            'txs': forms.Textarea(attrs={'class':'form-control'}),
            'adendums': forms.Textarea(attrs={'class':'form-control'}),
                        
        }


class ReevaluacionForm(forms.ModelForm):
    class Meta:
        model = Reevaluacion
        fields = ['paciente', 'genero', 'age', 'dxs_previos', 'immediate_background',
        'tension_sistolica', 'tension_diastolica', 'fc', 'fr', 'temp', 'saturacion', 'dextrostix', 'a1c', 'peso', 'estatura',
        'per_abdominal', 'expl', 'Doc1', 'Doc2', 'Doc3', 'Doc4', 'Doc5',
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
        fields = ['nombre', 'edad','genero', 'im_bkground', 'other_bkground', 'fr', 'O2', 'saturacion', 'fc', 'tension_sistolica', 'tension_diastolica', 'Diaforesis',
        'AVPU', 'apertura_ocular', 'Respuesta_Verbal', 'Respuesta_Motora', 'dextrostix', 'temp', 'peso', 'estatura', 'per_abdominal',
         'expl', 'dxs', 'MANEJO_INICIAL', 'Doc1', 'Doc2', 'Doc3', 'Doc4', 'Doc5', 'recetas', 'OBSERVACIONES_GENERALES', 'especialidad',
         'esp_otro' ]

        raw_id_fields = ('nombre', )
        autocomplete_fields = ('nombre',)
        widgets = {
                   
            'im_bkground': forms.Textarea(attrs={'class':'form-control', 
            'placeholder':'Describa por qué llegó el paciente, quien lo trajo o como llegó, qué sucedió antes (se desmayó, tuvo un accidente. empezó a sentirse mal...), describa el habitus exterior y los síntomas que el paciente pueda referir'}),
            'other_bkground': forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'Describa y recopile enfermedades previas, alergias y lo que considere importante'}),
            'expl': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Recomendamos iniciar con el hábitus exterior y describa lo relevante desde la cabeza a los pies'}),
            'dxs': forms.Textarea(attrs={'class':'form-control'}),
            'MANEJO_INICIAL': forms.Textarea(attrs={'class':'form-control'}),
            'immediate_background': forms.Textarea(attrs={'class':'form-control'}),
            'OBSERVACIONES_GENERALES': forms.Textarea(attrs={'class':'form-control'}),
         
                        
        }

class UrgReevForm(forms.ModelForm):
    class Meta:
        model = Urgencias_Reevaluaciones
        fields = ['paciente', 'edad', 'genero', 'evaluacion_sec', 'dxs_previos', 'sit_actual', 'fr', 'O2', 'saturacion', 'SaFI02', 'SaPaFI', 'vent_mec', 'mode', 'FrecResp',
        'Vt', 'PEEP', 'Sens', 'Pinsp', 'Tinsp', 'compl_ex', 'Rx_Torax', 'pH', 'pCO2', 'pO2', 'FIO2', 'Diaforesis',
        'fc', 'tension_sistolica', 'tension_diastolica', 'dextrostix', 'temp', 'peso', 'estatura', 'per_abdominal',
        'AVPU', 'apertura_ocular', 'Respuesta_Verbal', 'Respuesta_Motora', 'Sedacion', 'meds_dosis', 'RASS', 'hb', 'hto', 'leucocitos', 'neutrofilos',
        'basofilos', 'eosinofilos', 'linfocitos', 'glucosa', 'Urea', 'Creatinina', 'PCR', 'DHL', 'TGP', 'TGO', 'bilirrTot', 'Na', 'K', 'Ca','Mg',
        'P', 'Rx_descripcion', 'obs', 'dxs', 'reest_man', 'interconsultante1', 'interconsultante2', 'interconsultante3', 'Labs1', 'Labs2', 'Labs3', 'Labs4', 'Labs5', 'image1', 'image2', 'image3', 'image4',
        'image5', 'image6', 'image7', 'image8', 'image9', 'image10']

        raw_id_fields = ('paciente', )
        autocomplete_fields = ('paciente',)
        widgets = {
            'dxs_previos': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Copie y peque los Dxs de Ev. Primaria o de la última evalución subsecuente'}),
            'sit_actual': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Describa si hay algún cambio en la evolución clínica o cambios en el manejo con respecto a evaluación anterior'}),
            'compl_ex': forms.Textarea(attrs={'class':'form-control'}),
            'meds_dosis': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Mencione medicamentos y dosis de sedación'}),
            'obs': forms.Textarea(attrs={'class':'form-control'}),
            'Rx_descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'obs_neur': forms.Textarea(attrs={'class':'form-control'}),
            'dxs': forms.Textarea(attrs={'class':'form-control'}),
            'reest_man': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Indicaciones'}),

        }