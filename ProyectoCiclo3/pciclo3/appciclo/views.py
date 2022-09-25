from distutils.log import info
import json
from pydoc import cli
from django.shortcuts import render
from django.views import View
from .models import Contrasena, Empleado, Empresa, Rol, Ingreso, Egreso
from .models import Empleado
from .models import Empresa
from .models import Rol
from .models import Ingreso
from .models import Egreso

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


#creamos una clase con la tabla de empresas que permite ingresar datos
class EmpresaView(View):
    #se usa un metodo que evita el conflicto con los metodos de seguridad de django
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

#Se realizan las consualtas por medio de get, permite consulta general o por id enviada por la url
    def get(self,request,doc=0):
        if doc>0:
            empr=list(Empresa.objects.filter(IdEmpresa=doc).values())
            if len(empr)>0:
                emprrespuesta=empr[0]
                datos={"empresa":emprrespuesta}
            else:
                datos={"respuesta":"Dato no se encontro"}
        else:
             #datos={"empresa":clirespuesta}
            empr=list(Empresa.objects.values())
            datos={'listadoempresa':empr}
        return JsonResponse (datos)

#post enviamos los datos a la tabla por medio del body
    def post(self,request):
        datos=json.loads(request.body)
        Empresa.objects.create(IdEmpresa=datos["IdEmpresa"],Nombre=datos["Nombre"],Nit=datos["Nit"],Ciudad=datos["Ciudad"],Direccion=datos["Direccion"],Telefono=datos["Telefono"],SectorProductivo=datos["SectorProductivo"])
        return JsonResponse(datos)

#put se usa para modificar los datos
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
            mensaje={"Respuesta":"Datos Actualizado"}
        else:
            mensaje={"Respuesta":"Datos No Encontrados"}
        return JsonResponse(mensaje)


#eliminamos datos de la tabla
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

#se crea por metodoo get las opciones de hacer consultas general o por empleado
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

#Se crean nuevos usuarios 
    def post(self,request):
        datos=json.loads(request.body)
        empr=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
        rol=Rol.objects.get(IdRol=datos["IdRol"])
        pas=Contrasena.objects.get(IdContrasena=datos["IdContrasena"])
        Empleado.objects.create(IdEmpleado=datos["IdEmpleado"],Nombre=datos["Nombre"],Apellidos=datos["Apellidos"],Email=datos["Email"],Telefono=datos["Telefono"],Cargo=datos["Cargo"],FechaCreacion=datos["FechaCreacion"],FechaModificacion=datos["FechaModificacion"],IdEmpresa=empr, IdRol=rol, IdContrasena=pas)
        return JsonResponse(datos)

#
    def put(self,request,doc):
        datos=json.loads(request.body)
        try:
            empl=list(Empleado.objects.filter(IdEmpresa=doc).values())
            if len(empl)>0:
                 Empleados=Empleado.objects.get(IdEmpresa=doc)
                 Empleados.Nombre=datos["Nombre"]
                 Empleados.Apellidos=datos["Apellidos"]
                 Empleados.Email=datos["Email"]
                 Empleados.Telefono=datos["Telefono"]
                 Empleados.Cargo=datos["Cargo"]
                 Empresas=Empresa.objects.get(IdEmpresa=datos["IdEmpresa"])
                 rols=Rol.objects.get(IdRol=datos["IdRol"])
                 Contrasenas=Contrasena.objects.get(IdContrasena=datos["IdContrasena"])
                 Empleados.save()
                 mensaje={"Respuesta":"Datos Actualizado"}
            else:
                mensaje={"Respuesta":"Datos No Encontrados"}
            return JsonResponse(mensaje)

        except Empresa.DoesNotExist:
         aviso={"mensaje":"La linea no existe"}
        except Rol.DoesNotExist:
         aviso={"mensaje":"La linea no existe"}
        except Contrasena.DoesNotExist:
         aviso={"mensaje":"La linea no existe"}
        return JsonResponse(aviso)
