# Generated by Django 4.1 on 2022-09-29 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appciclo', '0004_remove_empleado_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='IdContrasena',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Contrasena',
        ),
    ]
