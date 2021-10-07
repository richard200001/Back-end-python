from django.contrib import admin
from .models.inventario import Inventario
from .models.usuario import Usuario
from .models.consulta import Consulta

admin.site.register(Usuario)
admin.site.register(Inventario)
admin.site.register(Consulta)
