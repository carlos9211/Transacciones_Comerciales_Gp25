# Generated by Django 4.1 on 2022-09-25 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appciclo', '0002_rename_role_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='Nit',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]