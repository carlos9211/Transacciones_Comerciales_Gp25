import json
from pydoc import cli
from django.shortcuts import render
from django.views import View
from .models import Empresa
from django.http.response import JsonResponse


#creamos una clase con la tabla de empresas que permite ingresar datos
#get se envian datos por medio de la url
class EmpresaView(View):
    def get(self,request):
        cli=list(Empresa.objects.values())
        datos={'listadoempresa':cli}
        return JsonResponse (datos)

#post enviamos los datos a la tabla por medio del body

    def post(self,request):
        datos=json.loads(request.body)
        Empresa.objects.create(IdEmpresa=datos["IdEmpresa"],Nombre=datos["Nombre"],Nit=datos["Nit"],Ciudad=datos["Ciudad"],Direccion=datos["Direccion"],Telefono=datos["Telefono"],SectorProductivo=datos["SectorProductivo"])
        return JsonResponse(datos)

#put se usa para modificar los datos
    def put(self,request,doc):
        datos=json.loads(request.body)
        cli=list(Empresa.objects.filter(IdEmpresa=doc).values())
        if len(cli)>0:
            Empresas=Empresa.objects.get(IdEmpresa=doc)
            Empresas.Nombre=datos["Nombre"]
            Empresas.Nit=datos["Nit"]
            Empresas.Ciudad=datos["Ciudad"]
            Empresas.Direccion=datos["Direccion"]
            Empresas.Telefono=datos["Telefono"]
            Empresas.SectorProductivo=datos["SectorProductivo"]
            Empresas.save()
            mensaje={"Respuesta":"Datos Actualizado"}
        else:
            mensaje={"Respuesta":"Datos No Encontrados"}
        return JsonResponse(mensaje)
        
# Create your views here.
