from django.urls import path
from .views import EmpleadoView, EmpresaView, EmpresaView

urlpatterns=[
    path('empresa/',EmpresaView.as_view(),name='Listar'),
    path('empresa/<int:doc>',EmpresaView.as_view(),name='actualizar'),
    path('empleado/',EmpleadoView.as_view(),name='guardar'),
    path('empleado/<int:doc>',EmpleadoView.as_view(),name='actualizar')

] 