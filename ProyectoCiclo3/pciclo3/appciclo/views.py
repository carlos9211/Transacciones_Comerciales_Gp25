from distutils.log import info
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.template import loader
from email import message
from pydoc import cli
from .models import Empleado, Empresa, Ingreso, Egreso

import json


#creamos una clase con la tabla de empresas que permite ingresar datos
class EmpresaView(View):
    #se usa un metodo que evita el conflicto con los metodos de seguridad de django
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

#Se realizan las consualtas por medio de get, permite consulta general o por id enviada por la url
    def get(self,request,doc=0):
        if doc > 0:
            listado = list(Empresa.objects.filter(IdEmpresa=doc).values())
            if len(listado) > 0:
                emprrespuesta = listado[0]
                template = "EmpresaBaseEmpleado.html"
                context = {"empresa": emprrespuesta}
            else:
                datos = {"respuesta":"Dato no se encontro"}
        else:
            #datos={"empresa":clirespuesta}
            listado = list(Empresa.objects.values())
            template = 'empresas.html'
            context = {'listado_empresas': listado}
        
        return render(request, template, context)

#post enviamos los datos a la tabla por medio del body
    def post(self,request):
        datos=json.loads(request.body)
        Empresa.objects.create(IdEmpresa=datos["IdEmpresa"],Nombre=datos["Nombre"],Nit=datos["Nit"],Ciudad=datos["Ciudad"],Direccion=datos["Direccion"],Telefono=datos["Telefono"],SectorProductivo=datos["SectorProductivo"])
        return JsonResponse(datos)

#put se usa para modificar los datos se envian por medio del body
    def put(self,request,doc):
        datos=json.loads(request.body)
        emp=list(Empresa.objects.filter(IdEmpresa=doc).values())
        if len(emp)>0:
            Empresas=Empresa.objects.get(IdEmpresa=doc)
            Empresas.Nombre=datos["Nombre"]
            Empresas.Nit=datos["Nit"]
            Empresas.Ciudad=datos["Ciudad"]
            Empresas.Direccion=datos["Direccion"]
            Empresas.Telefono=datos["Telefono"]
            Empresas.SectorProductivo=datos["SectorProductivo"]
            Empresas.save()
            mensaje={"Respuesta":"Datos Actualizados"}
        else:
            mensaje={"Respuesta":"Datos No Encontrados"}
        return JsonResponse(mensaje)


#eliminamos datos de la tabla, se envia por la url el id de los datos que deseamos eliminar
    def delete(self,request,doc):
        empr=list(Empresa.objects.filter(IdEmpresa=doc).values())
        if len(empr)>0:
            Empresa.objects.filter(IdEmpresa=doc).delete()
            mensaje={"Respuesta": "El Registro se Elimino"}
        else:
            mensaje={"Respuesta":"El  Registro no se Encontro"}
        return JsonResponse (mensaje)

class RolView(View):
#se usa un metodo que evita el conflicto con los metodos de seguridad de django
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

#Se realizan las consualtas por medio de get, permite consulta general o por id enviada por la url
    def get(self,request,IdRol=0):
        if IdRol>0:
            Rol=list(Rol)
            if len(Rol)>0:
                rolrespuesta=Rol[0]
                info={"empresa":rolrespuesta}
            else:
                info={"respuesta":"Dato no se encontro"}
        else:
             #datos={"empresa":clirespuesta}
            empr=list(Empresa.objects.values())
            info={'listadoempresa':empr}
        return JsonResponse (info)

#se crea un metodo con la tabla de empleados para los crud
class EmpleadoView(View):
    #se usa un metodo que evita el conflicto con los metodos de seguridad de django
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

#se crea por metodo get las opciones de hacer consultas general o por empleado enviando el id a consultar por la url
    def get(self,request,Id=0):
        if Id>0:
            empl=list(Empleado.objects.values())
            if len(empl)>0:
                emplrespuesta=empl[0]
                datos={"empleado":emplrespuesta}
            else:
                datos={"respuesta":"Dato no se encontro"}
        else:
             #datos={"empleado":clirespuesta}
            empl=list(Empleado.objects.values())
            datos={'listadoempleado':empl}
        return JsonResponse (datos)

#Se crean nuevos usuarios, se envian los datos por el body
    def post(self,request):
        datos=json.loads(request.body)
        empr=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
        Empleado.objects.create(IdEmpleado=datos["IdEmpleado"],Nombre=datos["Nombre"],Apellidos=datos["Apellidos"],Email=datos["Email"],Telefono=datos["Telefono"],Cargo=datos["Cargo"],FechaCreacion=datos["FechaCreacion"],FechaModificacion=datos["FechaModificacion"],IdEmpresa=empr, IdRol=datos["IdRol"], IdContrasena=datos["IdContrasena"])
        return JsonResponse(datos)

#Se modifican los datos de los empelados enviando por la url el id al que vamos a modificar
    def put(self,request,doc):
        datos=json.loads(request.body)
        try:
            empl=list(Empleado.objects.filter(IdEmpleado=doc).values())
            if len(empl)>0:
                 Empleados=Empleado.objects.get(IdEmpleado=doc)
                 Empleados.Nombre=datos["Nombre"]
                 Empleados.Apellidos=datos["Apellidos"]
                 Empleados.Email=datos["Email"]
                 Empleados.Telefono=datos["Telefono"]
                 Empleados.Cargo=datos["Cargo"]
                 Empresas=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
                 Empleados.IdRol=datos["IdRol"]
                 Empleados.IdContrasena=datos["IdContrasena"]
                 Empleados.save()
                 mensaje={"Respuesta":"Datos Actualizado"}
            else:
                mensaje={"Respuesta":"Datos No Encontrados"}
            return JsonResponse(mensaje)

        except Empresa.DoesNotExist:
         aviso={"mensaje":"La linea no existe"}
        return JsonResponse(aviso)

      
def loginusuario(request):
      if request.method=='POST':
         try:
            detalleusuario=Empleado.objects.get(Email=request.POST['Email'], IdContrasena=request.POST['IdContrasena'])
            if detalleusuario.IdRol=="Administrador":
               request.session['Email']=detalleusuario.Email
               request.session['documento']=detalleusuario.IdEmpleado
               return redirect(reverse('usuario'))
            #    return render(request, 'usuario.html')
            elif detalleusuario.IdRol=="Contador":
               request.session['Email']=detalleusuario.Email
               return render(request, 'movimientos.html')
            elif detalleusuario.IdRol=="General":
               request.session['Email']=detalleusuario.Email
               return render(request, 'general.html')   
         except Empleado.DoesNotExist as e:
            message.success(request,"No existe")
      return render(request,"ingreso.html")

def usuario(request):
    return render(request,"usuario.html")


#Se crea el metodo para registrar ingresos y modificarlos en caso de ser necesario
class IngresoView(View):
#se usa un metodo que evita el conflicto con los metodos de seguridad de django
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

#Se crean nuevos ingresos, estos se envian por el body
    def post(self,request):
        datos=json.loads(request.body)
        empr=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
        empl=Empleado.objects.get(IdRol=datos["IdEmpleado"])
        Ingreso.objects.create(IdIngreso=datos["IdIngreso"],Concepto=datos["Concepto"],Monto=datos["Monto"],FechaCreacion=datos["FechaCreacion"],FechaModificacion=datos["FechaModificacion"],IdEmpresa=empr, IdEmpleado=empl)
        return JsonResponse(datos)  

#Se modifican los Ingresos, enviando por la url el id al que vamos a modificar
    def put(self,request,doc):
        datos=json.loads(request.body)
        try:
            Ing=list(Ingreso.objects.filter(IdIngreso=doc).values())
            if len(Ing)>0:
                 Ingresos=Ingreso.objects.get(IdIngreso=doc)
                 Ingresos.Concepto=datos["Concepto"]
                 Ingresos.Monto=datos["Monto"]
                 Ingresos.FechaCreacion=datos["FechaCreacion"]
                 Ingresos.FechaModificacion=datos["FechaModificacion"]
                 Empresas=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
                 Empleados=Empleado.objects.get(IdRol=datos["IdEmpleado"])
                 Ingresos.save()
                 mensaje={"Respuesta":"Ingreso Actualizado"}
            else:
                mensaje={"Respuesta":"Ingreso No Encontrados"}
            return JsonResponse(mensaje)

        except Empresa.DoesNotExist:
         aviso={"mensaje":"La linea no existe"}
        return JsonResponse(aviso)

#Se crea el metodo para registrar Egresos y modificarlos en caso de ser necesario
class EgresoView(View):
#se usa un metodo que evita el conflicto con los metodos de seguridad de django
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

#Se crean nuevos ingresos, estos se envian por el body
    def post(self,request):
        datos=json.loads(request.body)
        empr=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
        empl=Empleado.objects.get(IdRol=datos["IdEmpleado"])
        Egreso.objects.create(IdEgreso=datos["IdEgreso"],Concepto=datos["Concepto"],Monto=datos["Monto"],FechaCreacion=datos["FechaCreacion"],FechaModificacion=datos["FechaModificacion"],IdEmpresa=empr, IdEmpleado=empl)
        return JsonResponse(datos)  

#Se modifican los Ingresos, enviando por la url el id al que vamos a modificar
    def put(self,request,doc):
        datos=json.loads(request.body)
        try:
            Egr=list(Egreso.objects.filter(IdEgreso=doc).values())
            if len(Egr)>0:
                 Egresos=Egreso.objects.get(IdEgreso=doc)
                 Egresos.Concepto=datos["Concepto"]
                 Egresos.Monto=datos["Monto"]
                 Egresos.FechaCreacion=datos["FechaCreacion"]
                 Egresos.FechaModificacion=datos["FechaModificacion"]
                 Empresas=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
                 Empleados=Empleado.objects.get(IdRol=datos["IdEmpleado"])
                 Egresos.save()
                 mensaje={"Respuesta":"Egreso Actualizado"}
            else:
                mensaje={"Respuesta":"Egreso No Encontrados"}
            return JsonResponse(mensaje)

        except Empresa.DoesNotExist:
         aviso={"mensaje":"La linea no existe"}
        return JsonResponse(aviso)

#
