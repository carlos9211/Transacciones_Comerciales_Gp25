import json
from pydoc import cli
from django.shortcuts import render
from django.views import View
from .models import Empresa
from django.http.response import JsonResponse

class EmpresaView(View):
    def get(self,request):
        cli=list(Empresa.objects.values())
        datos={'listadoempresa':cli}
        return JsonResponse (datos)


    def post(self,request):
        datos=json.loads(request.body)
        Empresa.objects.create(IdEmpresa=datos["IdEmpresa"],Nombre=datos["Nombre"],Nit=datos["Nit"],Ciudad=datos["Ciudad"],Direccion=datos["Direccion"],Telefono=datos["Telefono"],SectorProductivo=datos["SectorProductivo"])
        return JsonResponse(datos)
# Create your views here.
