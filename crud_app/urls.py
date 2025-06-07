from django.urls import path
from . import views

urlpatterns = [
    path('registro-atencion/', views.registro_atencion_view, name='registro_atencion'),
    path('exito/', views.exito, name='exito'),
    path('exportar-excel/', views.export_credentials_to_excel, name='export_credentials'),
    path('registro-atencion/', views.registro_atencion_view, name='registro-atencion'),
    path('', views.index, name='index'),
]