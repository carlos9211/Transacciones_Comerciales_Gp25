from datetime import datetime
from django.db import models


#TABLA DE EMPRESAS
class Empresas(models.Model):
    IdEmpresa=models.IntegerField(primary_key=True,max_length=20)
    Nit=models.CharField(max_length=10)
    DigitoVerificacion=models.CharField(max_length=1)
    Nombre=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=20)
    Direccion=models.CharField(max_length=100)
    Correo=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)

#TABLA DE ROLES
class Roles(models.Model):
    IdRol=models.IntegerField(primary_key=True, max_length=20)
    Nombre=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)  

#TABLA DE CONTRASENAS
class Contrasenas(models.Model):
    IdContrasena=models.IntegerField(primary_key=True, max_length=20)
    Contrasena=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)

#TABLA DE EMPLEADOS
class Empleados(models.Model):
    IdEmpleado=models.IntegerField(primary_key=True, max_length=20)
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Codigo=models.CharField(max_length=200)
    Telefono=models.CharField(max_length=20)
    Direccion=models.CharField(max_length=100)
    Correo=models.CharField(max_length=100)
    Cargo=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    IdRol=models.ForeignKey(Roles,on_delete=models.CASCADE)
    IdContrasena=models.ForeignKey(Contrasenas,on_delete=models.CASCADE)
    IdEmpresa=models.ForeignKey(Empresas,on_delete=models.CASCADE)

#TABLA DE INGRESOS
class Ingresos(models.Model):
    IdIngreso=models.IntegerField(primary_key=True,max_length=20)
    Valor=models.CharField(max_length=100)
    Concepto=models.CharField(max_length=300)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)    
    IdEmpresa=models.ForeignKey(Empresas,on_delete=models.CASCADE)
    IdEmpleado=models.ForeignKey(Empleados,on_delete=models.CASCADE)

#TABLA DE EGRESOS
class Egresos(models.Model):
    IdEgreso=models.IntegerField(primary_key=True,max_length=20)
    Valor=models.CharField(max_length=100)
    Concepto=models.CharField(max_length=300)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    IdEmpresa=models.ForeignKey(Empresas,on_delete=models.CASCADE)
    IdEmpleado=models.ForeignKey(Empleados,on_delete=models.CASCADE)
