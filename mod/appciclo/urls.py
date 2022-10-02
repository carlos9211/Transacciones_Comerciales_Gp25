from django.urls import path
from django.views import View
from . import views
from appciclo.models import Egreso
from .views import EgresoView, EmpleadoView, EmpresaView, EmpresaView, IngresoView

urlpatterns=[
    path('empresa/',EmpresaView.as_view(),name='Listar'),
    path('empresa/<int:doc>',EmpresaView.as_view(),name='actualizar'),
    path('empleado/',EmpleadoView.as_view(),name='guardar'),
    path('empleado/<int:doc>',EmpleadoView.as_view(),name='modificar'),
    path('ingreso/',IngresoView.as_view(),name='registrar'),
    path('ingreso/<int:doc>',IngresoView.as_view(),name='corregir'),
    path('egreso/',EgresoView.as_view(),name='registrar'),
    path('egreso/<int:doc>',EgresoView.as_view(),name='corregir'),
    path('usuario/',views.usuario,name='usuario'),
    #path('usuario/usuarioInfo.html',views.usuario,name='usuario'),
    path('login/',views.loginusuario ,name='login')


    

] 