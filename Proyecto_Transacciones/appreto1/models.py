from datetime import datetime
from django.db import models


#TABLA DE EMPRESAS
class Empresa(models.Model):
    IdEmpresa=models.IntegerField(max_length=20)
    Nit=models.CharField(max_length=10)
    DigitoVerificacion=models.CharField(max_length=1)
    Nombre=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=20)
    Direccion=models.CharField(max_length=100)
    Correo=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    

#TABLA DE EMPLEADOS
class Empleado(models.Model):
    IdEmpleado=models.IntegerField(max_length=20)
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Codigo=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=20)
    Direccion=models.CharField(max_length=100)
    Correo=models.CharField(max_length=100)
    Cargo=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    NombreEmpresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)

#TABLA DE USUARIOS
class Usuarios(models.Model):
    Nombre=models.CharField(max_length=20)
    Apellido=models.CharField(max_length=30)
    Documento=models.IntegerField()


#TABLA DE ROLES
class Roles(models.Model):
    Id_Rol=models.IntegerField(primary_key=True)
    rol=models.CharField(max_length=30)

#TABLA DE MOVIMIENTOS



# Create your models here.
