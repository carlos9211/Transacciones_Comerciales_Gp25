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
    rol=models.IntegerField()
    correo=models.CharField(max_length=50)
    celular=models.CharField(max_length=10)
    NombreEmpresa=models.ForeignKey(Empresa,on_delete=models.CASCADE)

#TABLA DE USUARIOS


#TABLA DE ROLES


#TABLA DE MOVIMIENTOS



# Create your models here.
