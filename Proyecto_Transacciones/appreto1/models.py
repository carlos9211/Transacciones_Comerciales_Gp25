from django.db import models


#TABLA DE EMPRESAS
class Empresa(models.Model):
    Id_empresa=models.IntegerField()
    Nit=models.IntegerField()
    NombreEmpresa=models.CharField(max_length=30)
    Direccion=models.CharField(max_length=50)
    Telefono=models.IntegerField()


#TABLA DE EMPLEADOS
class Empleado(models.Model):
    Nombre=models.CharField(max_length=30)
    Apellido=models.CharField(max_length=30)
    Documento=models.IntegerField()
    Id_rol=models.IntegerField()
    correo=models.CharField(max_length=50)
    celular=models.CharField(max_length=10)
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
