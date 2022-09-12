from datetime import datetime
from django.db import models

# Create your models here.

#TABLA DE EMPRESAS
class Empresa(models.Model):
    IdEmpresa=models.IntegerField(primary_key=True,max_length=20)
    Nombre=models.CharField(max_length=200)
    Nit=models.CharField(max_length=10) 
    Ciudad=models.CharField(max_length=50)
    Direccion=models.CharField(max_length=100)
    Telefono=models.CharField(max_length=20)
    SectorProductivo=models.CharField(max_length=50)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.IdEmpresa,self.Nombre,self.Nit,self.Ciudad,self.Direccion,self.Telefono,self.SectorProductivo,self.FechaCreacion,self.FechaModificacion

#TABLA DE ROLES
class Rol(models.Model):
    IdRol=models.IntegerField(primary_key=True, max_length=20)
    Nombre=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)  
    def __str__(self):
        return self.IdRol,self.Nombre,self.FechaCreacion,self.FechaModificacion

#TABLA DE CONTRASENAS
class Contrasena(models.Model):
    IdContrasena=models.IntegerField(primary_key=True, max_length=20)
    Contrasena=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.IdContrasena,self.Contrasena,self.FechaCreacion,self.FechaModificacion
#TABLA DE EMPLEADOS
class Empleado(models.Model):
    IdEmpleado=models.IntegerField(primary_key=True, max_length=20,unique=True)
    Imagen=models.ImageField()
    Nombre=models.CharField(max_length=100)
    Apellidos=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,unique=True)
    Telefono=models.CharField(max_length=20)
    Cargo=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    IdRol=models.ForeignKey(Rol,on_delete=models.CASCADE)
    IdContrasena=models.ForeignKey(Contrasena,on_delete=models.CASCADE)
    IdEmpresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)
    def __str__(self):
        return (self.IdEmpleado,self.Imagen,self.Nombre,self.Apellidos,self.Email,self.Telefono,self.Cargo,self.FechaCreacion,self.FechaModificacion,self.IdRol,self.IdContrasena,self.IdEmpresa)

#TABLA DE INGRESOS
class Ingreso(models.Model):
    IdIngreso=models.IntegerField(primary_key=True,max_length=20)
    Concepto=models.CharField(max_length=300)
    Monto=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)    
    IdEmpresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)
    IdEmpleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    def __str__(self):
        return self.IdIngreso,self.Concepto,self.Monto,self.FechaCreacion,self.FechaModificacion,self.IdEmpresa,self.IdEmpleado

#TABLA DE EGRESOS
class Egreso(models.Model):
    IdEgreso=models.IntegerField(primary_key=True,max_length=20)
    Concepto=models.CharField(max_length=300)
    Monto=models.CharField(max_length=100)
    FechaCreacion=models.DateTimeField(default=datetime.now)
    FechaModificacion=models.DateTimeField(default=datetime.now)
    IdEmpresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)
    IdEmpleado=models.ForeignKey(Empleado,on_delete=models.CASCADE)
    def __str__(self):
        return self.IdEgreso,self.Concepto,self.Monto,self.FechaCreacion,self.FechaModificacion,self.IdEmpresa,self.IdEmpleado