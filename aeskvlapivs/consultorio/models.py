
from ast import Break, Continue, If, Return
from email.policy import default
import os
from datetime import date
from tokenize import blank_re
from typing import Any, Type
from django.core.files.storage import FileSystemStorage
from django.db import models
from math import sqrt

fs = FileSystemStorage(location='/media/')

# Create your models here.
def generate_path(instance, filename):
    return os.path.join("upload", "id_" + str(instance.idupload), filename)

class Paciente(models.Model):
    FEMENINO= 'FEM'
    MASCULINO = 'MASC'
    GENERO = [(FEMENINO, 'Femenino'), (MASCULINO, 'Masculino')]  

    IMSS = 'IMSS'
    ISSSTE = 'ISSSTE'
    SecMarina = 'Secretaría de Marina'
    PEMEX = 'PEMEX'
    SEDENA = 'SEDENA'
    OTRO = 'Otro'
    DERECHOHABIENCIA = [(IMSS, 'IMSS'), (ISSSTE, 'ISSSTE'), (SecMarina, 'Secretaría de Marina'),
    (SEDENA, 'SEDENA'), (PEMEX, 'PEMEX'), (OTRO, 'Otro')]

    POSITIVO = 'POS'
    NEGATIVO = 'NEG' 
    REHAB = 'En Rehabilitación'
    OCACIONAL = 'Ocacional'
    SOCIAL = 'Social'
    SUSPENDIDO = 'Suspendido'
    AFIRMACION = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (REHAB, 'En Rehabilitación')] 
    AFIRMACION_TAB = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (SUSPENDIDO, 'Suspendido')] 
    AFIRMACION_SIMPLE = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo')]
    AFIRMACION_ALCOHOLISMO = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo'), (REHAB, 'En Rehabilitación'), 
    (OCACIONAL, 'Ocacional'), (SOCIAL, 'Social')]

    #Identificación

    name = models.CharField(max_length=100, verbose_name='Nombre')
    gender = models.CharField(max_length=4, choices=GENERO, verbose_name='Género')
    dob = models.DateField(verbose_name='Fecha de Nacimiento', blank=True, null=True)
    age = models.IntegerField(verbose_name='Edad', default=0, )
    nationality = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nacionalidad y Lugar de Nacimiento')
    etnia = models.CharField(max_length=50, blank=True, null=True, verbose_name='Etnia')
    scholarship = models.CharField(max_length=50, blank=True, null=True, verbose_name='Escolaridad')
    job = models.CharField(max_length=100, blank=True, null=True, verbose_name='Empleo')
    religion = models.CharField(max_length=50, blank=True, null=True, verbose_name='Religión')
    sport = models.CharField(max_length=50, blank=True, null=True, verbose_name='Deportes')
    civil_status = models.CharField(max_length=50, blank=True, null=True, verbose_name='Estado Civil')
    adress = models.CharField(max_length=2150, blank=True, null=True, verbose_name='Domicilio')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Teléfono', blank=True, null=True)
    entitlement = models.CharField(max_length=50, choices=DERECHOHABIENCIA, blank=True, null=True, verbose_name='Derechohabiencia')
    specify= models.CharField(max_length=30, verbose_name='Especifique otra derechohabiencia', blank=True, null=True)
    insurance = models.CharField(max_length=30, blank=True, null=True, verbose_name='Aseguradora')
    
    # Padeciemiento Actual

    immediate_background = models.TextField(verbose_name="Padecimiento, Razón de Abordaje o Situación Actual")

    #ANTECEDENTES

    smoking = models.CharField(max_length=20, choices=AFIRMACION_TAB, blank=True, null=True, verbose_name='Tabaquismo')
    alcohol = models.CharField(max_length=20,choices=AFIRMACION_ALCOHOLISMO, blank=True, null=True, verbose_name='Alcholismo')
    drugs_adictions = models.CharField(max_length=20,choices=AFIRMACION, blank=True, null=True, verbose_name='Adicciones')
    allergies = models.CharField(max_length=100,choices=AFIRMACION, blank=True, null=True, verbose_name='Alergias')
    dislipidemia = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True )
    dm = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Diabetes')
    hta = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='HTA')
    inf_ang_de_pecho = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Infartos o angina de pecho')
    evc = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Eventos Cerebrovasculares')
    ivp = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Insuficiencia vascular periférica')
    EPOC = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Enfermedad Pulmonar Obstructiva Crónica')
    cancer = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True, verbose_name='Cáncer')
    
    otras_enf = models.TextField(blank=True, null=True, verbose_name='Complemento, Otros Antecedentes y Enfermedades')
    cir_previas = models.CharField(max_length=200, blank=True, null=True, verbose_name='Cirugías previas')

    dxs_antec = models.TextField(blank=True, null=True, verbose_name='Resumen de Diagnósticos por Antecedentes', help_text='No esciriba aquí: Guarde para ver Resultados')

    obs = models.TextField(blank=True, null=True, verbose_name='Observaciones, otros antecedentes y tratamientos actuales')

    # Situación actual y Exploración

    actual_situation = models.TextField(verbose_name="Situación Actual y Exploración")

    tension_sistolica = models.IntegerField(blank=True, null=True, default=0)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    pam = models.IntegerField(default=0, verbose_name='PAM', help_text='No esciriba aquí: Guarde para ver Resultados')
    fc = models.IntegerField(blank=True, null=True, verbose_name='FC')
    fr= models.IntegerField(blank=True, null=True, verbose_name='FR')
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02')
    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix')

    A = 'Alerta'
    V = 'Respuesta Verbal'
    P = 'Respuesta al Dolor'
    U = 'Sin Respuesta'
    CONC = [(A, 'Alerta'), (V, 'Respuesta Verbal'), (P, 'Respuesta al Dolor'),
    (U, 'Sin Respuesta'),]
    AVPU =  models.CharField(max_length=50, choices=CONC, verbose_name='Estado de Conciencia', blank=True, null=True)

    a1c = models.CharField(max_length=5, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True, default=0) 
    estatura = models.FloatField(blank=True, null=True, default=1)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC', help_text='No esciriba aquí: Guarde para ver Resultados')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Clasificación Masa Corporal', help_text='No esciriba aquí: Guarde para ver Resultados')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC', help_text='No esciriba aquí: Guarde para ver Resultados')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')

    # Paraclínicos

    Imagenología1 = models.FileField(upload_to='Paciente/',help_text='formato jpg, jpge', blank=True, null=True )
    Imagenología2 = models.FileField(upload_to='Paciente/', help_text='formato jpg, jpge',blank=True, null=True)
    Imagenología3 = models.FileField(upload_to='Paciente/',help_text='formato jpg, jpge',blank=True, null=True)

    Labs1 = models.FileField(upload_to='Paciente/', help_text='formato pdf',blank=True, null=True)
    Labs2 = models.FileField(upload_to='Paciente/', help_text='formato pdf', blank=True, null=True)
    recetas = models.FileField(upload_to='Paciente/', help_text='formato pdf',blank=True, null=True, verbose_name='Recetas')

    #Diagnóticos y Tx

    diagnosis = models.TextField(verbose_name='Diagnósticos')
    obs = models.TextField(verbose_name="Observaciones")
    txs = models.TextField(verbose_name='Manejos y Tratamientos')

    adendums = models.TextField(blank=True, null=True)

    RECOMENDACIONES = models.CharField(max_length=150, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    reevaluación = models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')
    
    antecedentes = ['smoking', 'alcohol', 'drugs_adictions', 'allergies', 'dislipidemia', 'dm', 'hta,',
      'inf_ang_de_pecho', 'evc', 'ivp', 'EPOC', 'cancer', ]

    



    @property
    def tabaquismo(self):
        if self.smoking == 'POS':
            POS = 'TABAQUISMO'
            return POS

        
    @property
    def alcoholismo(self):
        if self.alcohol == 'POS':
            return 'ALCOHOLISMO ACTIVO'
                
        
    @property
    def adiccion(self):
        if self.drugs_adictions == 'POS':
            POS = 'ESPECIFIQUE LAS ADICCIONES'
            return POS
                
    
    @property
    def alergias(self):
        if self.allergies == 'POS':
            POS = 'ESPECIFIQUE ALERGIAS'
            return POS

    @property
    def dislpid (self):
        if self.dislipidemia == 'POS':
            POS = 'DISLIPIDEMIA'
            return POS
                
            
    @property
    def diabetes(self):
        if self.dm == 'POS':
            POS = 'DIABETES MELLITUS'
            return POS
            
                
    
    @property
    def hipertension (self):
        if self.hta == 'POS': 
            POS = 'HTA'
            return POS
                

    @property
    def cardiopatia(self):
        if self.inf_ang_de_pecho == 'POS':
            POS = 'CARDIOPATIA ISQUEMICA'
            return POS


    @property
    def encefalopatía(self):
        if self.evc == 'POS':
            POS = 'ENCEFALOPATIA VASCULAR'
            return POS
                

    @property
    def insuf_vasc(self):
        if self.ivp == 'pos':
            POS = 'INSUFICIENCIA VASCULAR PERIFERICA'
            return POS
                    

    @property
    def enf_pulm(self):
        if self.EPOC == 'POS':
            POS = 'EPOC'
            return POS

    @property
    def onc(self):
        if self.cancer == 'POS':
            POS = 'ESPECIFIQUE DATOS DEL CANCER'
            return POS

    @property
    def calculateAge(self): 
        today = date.today() 
        age = today.year - self.dob.year - ((today.month, today.day) < 
            (self.dob.month, self.dob.day))  
        return age 

    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 

    @property
    def masa_corporal(self):
        return self.peso/self.estatura ** 2

    #def masa_corporal(self):
        return self.peso/self.estatura ** 2


    @property
    def area_sup_corp(self):
        return sqrt (self.peso * (self.estatura * 100) / 3600)

    @property
    def imc_clasif(self):
        if self.imc < 18.5 and self.imc > 1:
            return 'Desnutrición'
        
        elif self.imc >18.5 and self.imc <25:
            return 'Normal'

        elif self.imc >25 and self.imc < 27:
            return 'Sobrepeso Grado I'

        elif self.imc >27 and self.imc < 30:
            return 'Sobrepeso Grado II'

        elif self.imc >30 and self.imc < 35:
            return 'Obesidad Tipo I'

        elif self.imc >35 and self.imc < 40:
            return 'Obesidad Tipo II'

        elif self.imc >40 and self.imc < 50:
            return 'Obesidad Tipo III-Mórbida'

        elif self.imc >50:
            return 'Obesidad Tipo IV-Extrema'
        elif self.imc < 1:
            return 'Hay que pesar al paciente'

    @property
    def clhta(self):
        if self.tension_diastolica >90 and self.tension_diastolica< 104:
            return 'Hipertensión Leve ' 

        elif self.tension_diastolica > 104 and self.tension_diastolica< 114:
            return 'Hipertensión Moderada, '

        elif self.tension_diastolica > 114:
            return 'Hipertensión Severa / Descarte Crisis Hipertensiva '

        else:
            return ''

    @property
    def qsofa(self):
        if self.tension_sistolica < 100 and self.AVPU == 'Respuesta Verbal' or self.AVPU == 'Respuesta al Dolor' and self.fr >22:
            return 'qSOFA indica que hay que descartar Sepsis'


    def save(self):
        self.age = self.calculateAge
        self.imc = self.masa_corporal
        self.climc = self.imc_clasif
        self.asc = self.area_sup_corp
        self.pam = self.presion_media
        self.dxs_antec = (self.tabaquismo, self.alcoholismo, self.alergias, self.dislpid, 
        self.diabetes, self.hipertension, self.cardiopatia, self.insuf_vasc, self.enf_pulm, self.onc)
        self.RECOMENDACIONES = self.clhta, self.qsofa
        super(Paciente, self).save()

    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-timestamp',)
        verbose_name_plural='a) Pacientes'

    

class Reevaluacion(models.Model):
    IMSS = 'IMSS'
    ISSSTE = 'ISSSTE'
    SecMarina = 'Secretaría de Marina'
    PEMEX = 'PEMEX'
    SEDENA = 'SEDENA'
    OTRO = 'Otro'
    DERECHOHABIENCIA = [(IMSS, 'IMSS'), (ISSSTE, 'ISSSTE'), (SecMarina, 'Secretaría de Marina'),
    (SEDENA, 'SEDENA'), (PEMEX, 'PEMEX'), (OTRO, 'Otro')]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    age = models.SmallIntegerField(default=0, verbose_name='Edad')

    entitlement = models.CharField(max_length=50, choices=DERECHOHABIENCIA, blank=True, null=True, verbose_name='Derechohabiencia')

    specify= models.CharField(max_length=30, verbose_name='Especifique otra derechohabiencia', blank=True, null=True)
    
    phone = models.CharField(max_length=15, verbose_name='Teléfono', blank=True, null=True)

    email = models.EmailField(blank=True, null=True)

    dxs_previos = models.TextField (blank=True, null=True)

    immediate_background = models.TextField(verbose_name="Padecimiento o Situación Actual")

    tension_sistolica = models.PositiveSmallIntegerField(blank=True, null=True, default=1)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=1)
    pam = models.IntegerField(default=0, verbose_name='PAM')
    fc = models.IntegerField(blank=True, null=True, verbose_name='FC')
    fr= models.IntegerField(blank=True, null=True, verbose_name='FR')
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02')
    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix', default=0)
    a1c = models.CharField(max_length=5, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True, default=0) 
    estatura = models.FloatField(blank=True, null=True, default=1)
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Clasificación Masa Corporal')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')
    expl = models.TextField(verbose_name='Complemente Exploración', blank=True, null=True)


     # Paraclínicos

    Imagenología1 = models.FileField(upload_to='Reevalucion', help_text='formato jpg, jpge', blank=True, null=True)
    Imagenología2 = models.FileField(upload_to='Reevalucion', help_text='formato jpg, jpge', blank=True, null=True)
    Imagenología3 = models.FileField(upload_to='Reevalucion', help_text='formato jpg, jpge', blank=True, null=True)

    Labs1 = models.FileField(upload_to='Reevalucion', help_text='formato pdf, jpg, jpge', blank=True, null=True)
    Labs2 = models.FileField(upload_to='Reevalucion',help_text='formato pdf, jpg, jpge', blank=True, null=True)
    recetas = models.FileField(upload_to='Reevalucion', help_text='formato pdf, jpg, jpge', blank=True, null=True, verbose_name='Recetas')

    #Diagnóticos y Tx

    diagnosis = models.TextField(verbose_name='Diagnósticos')
    obs = models.TextField(verbose_name="Observaciones")
    txs = models.TextField(verbose_name='Manejos y Tratamientos')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    reevaluación = models.DateTimeField(blank=True, null=True, verbose_name='prox. reevaluación')


    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 

    @property
    def masa_corporal(self):
        return self.peso/self.estatura ** 2

    @property
    def imc_clasif(self):
        if self.imc < 18.5 and self.imc > 1:
            return 'Desnutrición'
        
        elif self.imc >18.5 and self.imc <25:
            return 'Normal'

        elif self.imc >24.9 and self.imc < 27:
            return 'Sobrepeso Grado I'

        elif self.imc > 27 and self.imc < 30:
            return 'Sobrepeso Grado II'

        elif self.imc >30 and self.imc < 35:
            return 'Obesidad Tipo I'

        elif self.imc >35 and self.imc < 40:
            return 'Obesidad Tipo II'

        elif self.imc >40 and self.imc < 50:
            return 'Obesidad Tipo III-Mórbida'

        elif self.imc >50:
            return 'Obesidad Tipo IV-Extrema'
        elif self.imc < 1:
            return 'Hay que pesar al paciente'


    @property
    def area_sup_corp(self):
        return sqrt (self.peso * (self.estatura * 100) / 3600)


    def save(self):
        self.imc = self.masa_corporal
        self.climc = self.imc_clasif
        self.asc = self.area_sup_corp
        self.pam = self.presion_media
        super(Reevaluacion, self).save()
       
        

    
    def __str__(self):
        return self.paciente.name

    class Meta:
        ordering = ('-timestamp',)
        verbose_name_plural='b) Reevaluación'


#URGENCIAS



class Urgencias(models.Model):
    nombre = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    edad = models.SmallIntegerField(default=0)

    im_bkground = models.TextField(verbose_name='Antecedentes Inmediatos')

    other_bkground = models.TextField(verbose_name='Otros Antecedentes')

    tension_sistolica = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    pam = models.IntegerField(default=0, verbose_name='PAM', help_text='No escriba aquí')

    POSITIVO = 'POS'
    NEGATIVO = 'NEG' 
    AFIRMACION_SIMPLE = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo')]
    Diaforesis = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True )


    fc = models.IntegerField(default=0, blank=True, null=True, verbose_name='FC')
    fr= models.IntegerField(default=0, blank=True, null=True, verbose_name='FR')
    O2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True, help_text='En litros/min')
    FiO2 = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, default=.21, help_text= 'No escriba aquí')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02', default=1)
    SpFI = models.PositiveSmallIntegerField(blank=True, null=True, help_text='No escriba aquí')
    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix', default=0)
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    peso = models.FloatField(blank=True, null=True, default=0, help_text='Si no puede pesar al paciente, calcule un aproximado') 
    estatura = models.FloatField(blank=True, null=True, default=1, help_text='En metros y cms')
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC', help_text='No escriba aquí')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Clasificación Masa Corporal', help_text='No escriba aquí')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC', help_text='No escriba aquí')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')


    #COMPONENTE NEUROLOGICO
    A = 'Alerta'
    V = 'Respuesta Verbal'
    P = 'Respuesta al Dolor'
    U = 'Sin Respuesta'
    CONC = [(A, 'A Alerta'), (V, 'V Respuesta Verbal'), (P, 'P Respuesta al Dolor'),
    (U, 'U Sin Respuesta'),]
    AVPU =  models.CharField(max_length=50, choices=CONC, verbose_name='Estado de Conciencia', blank=True, null=True)

    #PARAMETROS DE GLASGOW
    Espontanea = 4
    Orden_verbal = 3
    Est_doloroso = 2
    No_apertura = 1
    AP_OCULAR = [(Espontanea, 4 ), (Orden_verbal, 3), (Est_doloroso, 2), (No_apertura, 1)]
    apertura_ocular = models.PositiveSmallIntegerField(choices=AP_OCULAR, blank=True, null=True, default=1, help_text='Espontánea 4; Orden verbal 3; Est. Doloroso 2; No Apertura 1.')

    Orientado = 5
    Desorientado_Confuso = 4
    Incoherente = 3
    Sonidos_incomprensibles = 2
    Ausencia_Respuesta = 1
    RESP_VERBAL = [(Orientado, 5), (Desorientado_Confuso, 4), (Incoherente, 3), (Sonidos_incomprensibles, 2), 
    (Ausencia_Respuesta, 1),]
    Respuesta_Verbal = models.PositiveSmallIntegerField(blank=True, null=True, default=1, choices=RESP_VERBAL, help_text='Orientado 5; Desorientado confuso 4; Incoherente 3; Sonidos incomprensibles 1.')

    Obedece_ordenes = 6
    Localiza_dolor = 5
    Retirada_al_dolor = 4
    Flexion_anormal = 3
    Extension_anormal = 2
    Ausencia_respuesta = 1
    RESP_MOTORA = [(Obedece_ordenes, 6), (Localiza_dolor, 5), (Retirada_al_dolor, 4), (Flexion_anormal, 3),
    (Extension_anormal, 2), (Ausencia_respuesta, 1),]
    Respuesta_Motora = models.PositiveSmallIntegerField(choices=RESP_MOTORA, default=1, blank=True, null=True, help_text='Obedece órdenes 6; Localiza dolor 5; Retirada al dolor 4; Flexión anormal 3; Extensión anormal 2; Ausencia de Respuesta 1.')

    ESCALA_DE_GLASGOW = models.PositiveSmallIntegerField(blank=True, null=True, help_text='sume los parámetros')

    expl = models.TextField(verbose_name='Complemente Exploración', blank=True, null=True)

    dxs = models.TextField(blank=True, null=True, verbose_name='DIAGNOSTICOS')

    MANEJO_INICIAL = models.TextField(blank=True, null=True)

    OBSERVACIONES_GENERALES = models.TextField(blank=True, null=True,)

    NEUROLOGICO = models.CharField(max_length=100, blank=True, null=True, help_text='No escriba aquí')

    RESPIRATORIO = models.CharField(max_length=100, blank=True, null=True, help_text='No escriba aquí')

    HEMODINAMICO = models.CharField(max_length=100, blank=True, null=True, help_text='No escriba aquí')

    INFECCIOSO = models.CharField(max_length=100, blank=True, null=True, help_text='No escriba aquí')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Fecha de Registro')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')


    @property
    def masa_corporal(self):
        return self.peso/self.estatura ** 2

        #float division by zero

    @property
    def imc_clasif(self):
        if self.imc < 18.5 and self.imc > 1:
            return 'Desnutrición'
        
        elif self.imc >18.5 and self.imc <25:
            return 'Normal'

        elif self.imc >24.9 and self.imc < 27:
            return 'Sobrepeso Grado I'

        elif self.imc > 27 and self.imc < 30:
            return 'Sobrepeso Grado II'

        elif self.imc >30 and self.imc < 35:
            return 'Obesidad Tipo I'

        elif self.imc >35 and self.imc < 40:
            return 'Obesidad Tipo II'

        elif self.imc >40 and self.imc < 50:
            return 'Obesidad Tipo III-Mórbida'

        elif self.imc >50:
            return 'Obesidad Tipo IV-Extrema'
        elif self.imc < 1:
            return 'Hay que pesar al paciente'

    @property
    def area_sup_corp(self):
        return sqrt (self.peso * (self.estatura * 100) / 3600)
    
    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 
    
    @property
    def consid(self):
        if self.ESCALA_DE_GLASGOW < 9:
            return 'Considere Manejo Avanzado de Vía Aérea y/o Reevalúe Glasgow'
    
    @property
    def shock(self):
        if self.pam < 70 and self.fc >95 and self.Diaforesis == 'POS' :
            return 'Descarte Estado de Choque o asegúrese de haber checado TA y FC '

        else:
            return ''

    @property
    def hta(self):
        if self.tension_diastolica >90 and self.tension_diastolica< 104:
            return 'Hipertensión Leve ' 

        if self.tension_diastolica > 104 and self.tension_diastolica< 114:
            return 'Hipertensión Moderada, '

        if self.tension_diastolica > 114:
            return 'Hipertensión Severa / Descarte Crisis Hipertensiva '

        else:
            return ''

    @property
    def fio2(self):
        return (3 * self.O2 + 21) / 100

        #unsupported operand type(s) for *: 'int' and 'NoneType'

    @property
    def spfi(self):
        return self.saturacion / self.FiO2

        #unsupported operand type(s) for /: 'NoneType' and 'float'

    @property
    def sira(self):
        if self.SpFI < 419 and self.fr > 20:
            return 'Disfunción Respiratoria, Realice Gasometría'

    @property
    def glasgow(self):
        return self.apertura_ocular + self.Respuesta_Verbal + self.Respuesta_Motora 


    @property
    def qsofa(self):
        if self.tension_sistolica < 100 and self.ESCALA_DE_GLASGOW < 15 and self.fr >22:
            return 'Si paciente no es de Trauma: qSOFA indica que hay que descartar Sepsis'

    def save(self):
        self.pam = self.presion_media
        self.FiO2 = self.fio2
        self.SpFI = self.spfi
        self.imc = self.masa_corporal
        self.asc = self.area_sup_corp
        self.climc = self.imc_clasif
        self.ESCALA_DE_GLASGOW = self.glasgow
        self.NEUROLOGICO = self.consid
        self.RESPIRATORIO = self.sira
        self.HEMODINAMICO = self.shock, self.hta
        self.INFECCIOSO = self.qsofa
        super(Urgencias, self).save()
        

    def __str__(self):
        return self.nombre.name
        

    class Meta:
        ordering = ('-timestamp',)       
        verbose_name_plural='c) Urgencias, Evaluación Primaria'
        






# REEVALUACIONES DE URGENCIAS

class Urgencias_Reevaluaciones(models.Model):
    ev_1 = 'Primera Evaluación'
    ev_2 = 'Segunda Evaluación'
    ev_3 = 'Tercera Evaluación'
    ev_4 = 'Cuarta Evaluación'
    ev_5 = 'Quinta Evaluación'
    ev_6 = 'Sexta Evaluación'
    ev_7 = 'Séptima Evaluación'
    ev_8 = 'Octava Evaluación'
    REEV_SECS = [(ev_1, 'Primera Evaluación'), (ev_2, 'Segunda Evaluación'), (ev_3, 'Tercera Evalaución'),
    (ev_4, 'Cuarta Evaluación'), (ev_5, 'Quinta Evaluación'), (ev_6, 'Sexta Evaluación'), (ev_7, 'Séptima Evaluación'),
    (ev_8, 'Octava Evaluación')]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    edad = models.SmallIntegerField(default=0)
    evaluacion_sec = models.CharField(max_length=50, choices=REEV_SECS, blank=True, null=True, verbose_name='Evaluación Subsecuente')
    dxs_previos = models.TextField(blank=True, null=True)
    sit_actual = models.TextField(blank=True, null=True, verbose_name='Situación Actual')

# REEXPLORACION FISICA

    

    POSITIVO = 'POS'
    NEGATIVO = 'NEG' 
    AFIRMACION_SIMPLE = [ (POSITIVO, 'Positivo'), (NEGATIVO, 'Negativo')]
    Diaforesis = models.CharField(max_length=100,choices=AFIRMACION_SIMPLE, blank=True, null=True )

    fr= models.IntegerField(default=0, blank=True, null=True, verbose_name='FR')
    O2 = models.PositiveSmallIntegerField(default=0, blank=True, null=True, help_text='En litros/min')
    FiO2 = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, default=.21, help_text= 'No escriba aquí')
    saturacion = models.IntegerField(blank=True, null=True, verbose_name='Sa02', default=1)
    SpFI = models.PositiveSmallIntegerField(blank=True, null=True, help_text='No escriba aquí')

    @property
    def spfi(self):
        return self.saturacion / self.FiO2

        #unsupported operand type(s) for /: 'NoneType' and 'float'

    @property
    def sira(self):
        if self.SpFI < 419 and self.fr > 20:
            return 'Disfunción Respiratoria, Realice Gasometría'
    
    fc = models.IntegerField(default=0, blank=True, null=True, verbose_name='FC')
    tension_sistolica = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    tension_diastolica = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    pam = models.IntegerField(default=0, verbose_name='PAM', help_text='No escriba aquí')

    @property
    def presion_media(self):
        return (self.tension_sistolica + (2 * self.tension_diastolica))/3 

    @property
    def shock(self):
        if self.pam < 70 and self.fc >95 and self.Diaforesis == 'POS' :
            return 'Descarte Estado de Choque o asegúrese de haber checado TA y FC '

        else:
            return ''

    @property
    def hta(self):
        if self.tension_diastolica >90 and self.tension_diastolica< 104:
            return 'Hipertensión Leve ' 

        if self.tension_diastolica > 104 and self.tension_diastolica< 114:
            return 'Hipertensión Moderada, '

        if self.tension_diastolica > 114:
            return 'Hipertensión Severa / Descarte Crisis Hipertensiva '

        else:
            return ''

    dextrostix = models.IntegerField(blank=True, null=True, verbose_name='Dextrostix', default=0)
    temp =  models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, verbose_name='Temp')
    peso = models.FloatField(blank=True, null=True, default=0, help_text='Si no puede pesar al paciente, calcule un aproximado') 
    estatura = models.FloatField(blank=True, null=True, default=1, help_text='En metros y cms')
    imc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='IMC', help_text='No escriba aquí')
    climc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Clasificación Masa Corporal', help_text='No escriba aquí')
    asc = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='ASC', help_text='No escriba aquí')
    per_abdominal = models.IntegerField(blank=True, null=True, verbose_name='Per. Abd en cms')

    @property
    def peso_urg1(Urgencias):
        return Urgencias.peso

    @property
    def estatura_urg1(Urgencias):
        return Urgencias.estatura

    @property
    def imc_urg1(Urgencias):
        return Urgencias.imc

    @property
    def climc_urg1(Urgencias):
        return Urgencias.climc
    
    @property
    def asc_urg1(Urgencias):
        return Urgencias.asc

    @property
    def fio2(self):
        return (3 * self.O2 + 21) / 100


    A = 'Alerta'
    V = 'Respuesta Verbal'
    P = 'Respuesta al Dolor'
    U = 'Sin Respuesta'
    CONC = [(A, 'A Alerta'), (V, 'V Respuesta Verbal'), (P, 'P Respuesta al Dolor'),
    (U, 'U Sin Respuesta'),]
    AVPU =  models.CharField(max_length=50, choices=CONC, verbose_name='Estado de Conciencia', blank=True, null=True)

    #PARAMETROS DE GLASGOW
    Espontanea = 4
    Orden_verbal = 3
    Est_doloroso = 2
    No_apertura = 1
    AP_OCULAR = [(Espontanea, 4 ), (Orden_verbal, 3), (Est_doloroso, 2), (No_apertura, 1)]
    apertura_ocular = models.PositiveSmallIntegerField(choices=AP_OCULAR, blank=True, null=True, default=1, help_text='Espontánea 4; Orden verbal 3; Est. Doloroso 2; No Apertura 1.')

    Orientado = 5
    Desorientado_Confuso = 4
    Incoherente = 3
    Sonidos_incomprensibles = 2
    Ausencia_Respuesta = 1
    RESP_VERBAL = [(Orientado, 5), (Desorientado_Confuso, 4), (Incoherente, 3), (Sonidos_incomprensibles, 2), 
    (Ausencia_Respuesta, 1),]
    Respuesta_Verbal = models.PositiveSmallIntegerField(blank=True, null=True, default=1, choices=RESP_VERBAL, help_text='Orientado 5; Desorientado confuso 4; Incoherente 3; Sonidos incomprensibles 1.')

    Obedece_ordenes = 6
    Localiza_dolor = 5
    Retirada_al_dolor = 4
    Flexion_anormal = 3
    Extension_anormal = 2
    Ausencia_respuesta = 1
    RESP_MOTORA = [(Obedece_ordenes, 6), (Localiza_dolor, 5), (Retirada_al_dolor, 4), (Flexion_anormal, 3),
    (Extension_anormal, 2), (Ausencia_respuesta, 1),]
    Respuesta_Motora = models.PositiveSmallIntegerField(choices=RESP_MOTORA, default=1, blank=True, null=True, help_text='Obedece órdenes 6; Localiza dolor 5; Retirada al dolor 4; Flexión anormal 3; Extensión anormal 2; Ausencia de Respuesta 1.')

    ESCALA_DE_GLASGOW = models.PositiveSmallIntegerField(blank=True, null=True, help_text='sume los parámetros')

    @property
    def glasgow(self):
        return self.apertura_ocular + self.Respuesta_Verbal + self.Respuesta_Motora

    @property
    def consid(self):
        if self.ESCALA_DE_GLASGOW < 9:
            return 'Considere Manejo Avanzado de Vía Aérea y/o Reevalúe Glasgow'

    @property
    def qsofa(self):
        if self.tension_sistolica < 100 and self.ESCALA_DE_GLASGOW < 15 and self.fr >22:
            return 'Si paciente no es de Trauma: qSOFA indica que hay que descartar Sepsis'





    def save(self):
        self.peso = self.estatura_urg1
        self.estatura =self.estatura_urg1
        self.pam = self.presion_media
        self.FiO2 = self.fio2
        self.SpFI = self.spfi
        self.imc = self.imc_urg1
        self.asc = self.asc_urg1
        self.climc = self.imc_urg1
        self.ESCALA_DE_GLASGOW = self.glasgow
        self.NEUROLOGICO = self.consid
        self.RESPIRATORIO = self.sira
        self.HEMODINAMICO = self.shock, self.hta
        self.INFECCIOSO = self.qsofa
        super(Urgencias_Reevaluaciones, self).save()

    
            






