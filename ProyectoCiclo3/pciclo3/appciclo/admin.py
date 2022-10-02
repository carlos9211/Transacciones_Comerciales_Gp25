from django.contrib import admin
from .models import Empresa
from .models import Empleado
from .models import Ingreso
from .models import Egreso



# Register your models here.
admin.site.register(Empresa)
admin.site.register(Empleado)
admin.site.register(Ingreso)
admin.site.register(Egreso)