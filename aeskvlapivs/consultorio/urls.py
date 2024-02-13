from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (PacienteListView, PacienteDetailView, PacienteCreate, PacienteUpdate, PacienteDeleteView, SearchResultsView, 
SearchReevResultsView, ReevaluacionListView, ReevalucionDetailView, ReevaluacionUpdate, ReevaluacionCreate, ReevalucionDeleteView, SearchUrgenciasReevResultsView, 
UrgenciasListView, UrgenciasCreate, UrgenciasDetailView, UrgenciasReevDetail, UrgenciasUpdate, UrgenciasDeleteView, SearchUrgenciasResultsView, 
UrgenciasReevListView, UrgenciasReevDetail, SearchUrgenciasReevResultsView, UrgReevCreate, UrgenciasReevUpdate, UrgReevDelete, HistClinica
)


app_name = "consultorio"

consultorio_patterns = ([
    path('', PacienteListView.as_view(), name='pacientes'), 
    path('create/', PacienteCreate.as_view(),name='nuevo_paciente'),
    path('<int:pk>/<slug:paciente_slug>/', PacienteDetailView.as_view(), name='paciente'),
    path('update/<int:pk>/', PacienteUpdate.as_view(),name='actualizar_paciente'),
    path('delete/<int:pk>/', PacienteDeleteView.as_view(),name='eliminar_paciente'),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("upload_pac", views.uploadFilePac, name = "uploadFile_pac"), 
    
    path('historia_clinica/ <int:pk>', HistClinica.as_view(), name='historia_clinica'),    
    
    path('reevaluaciones/', ReevaluacionListView.as_view(), name='reevaluaciones'),
    path('create_reev/', ReevaluacionCreate.as_view(),name='nueva_reevaluacion'),
    path('<int:pk>/', ReevalucionDetailView.as_view(), name='reevaluacion'),
    path('update_reevaluacion/<int:pk>/', ReevaluacionUpdate.as_view(),name='Actualizar_reevaluacion'),    
    path('delete_reev/<int:pk>/', ReevalucionDeleteView.as_view(),name='eliminar reevaluacion'),
    path("search_reev/", SearchReevResultsView.as_view(), name="search_results_reev"),
    path("upload_reev", views.uploadFileReev, name = "uploadFile_reev"),

    path('urgencias/', UrgenciasListView.as_view(), name='pacientes_urgencias'),
    path('create_urgencias/', UrgenciasCreate.as_view(),name='nueva_urgencia'),
    path('<int:pk>/slugify', UrgenciasDetailView.as_view(), name='urgencias'),
    path('update_urgencias/<int:pk>/', UrgenciasUpdate.as_view(),name='actualizar_urgencia'),    
    path('delete_urgencias/<int:pk>/', UrgenciasDeleteView.as_view(),name='eliminar_urgencia'),
    path("search_urgencias/", SearchUrgenciasResultsView.as_view(), name="search_results_urgencias"),
    path("upload_urgencias", views.uploadFileUrgencias, name = "uploadFile_urgencias"),

    path('urgencias_eval_secs/', UrgenciasReevListView.as_view(), name='urg_eval_subs'),
    path('urgreev_create/',UrgReevCreate.as_view(), name='urgreev_create' ),
    path('<int:pk>/<slug:urgencias_reevaluaciones_slug>', UrgenciasReevDetail.as_view(), name='urgencias_reev_detail'),
    path('delete_urgenciareev/<int:pk>/', UrgReevDelete.as_view(), name='delete_urgenciareev'),
    path('update_urgenciareev/<int:pk>/', UrgenciasReevUpdate.as_view(), name='update_urgenciareev'),
    path('search_urgreev/', SearchUrgenciasReevResultsView.as_view(), name= 'search_results_urgenciasreev'),  
    path("upload_urgenciasreev", views.uploadFileUrgenciasReev, name = "uploadFile_urgenciasreev"),
    
    

   
], 'consultorio')




