from django.urls import path
from .views import EmpresaView, EmpresaView

urlpatterns=[
    path('empresa/',EmpresaView.as_view(),name='Listar')

]