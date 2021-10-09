from django.db import models


class Inventario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length= 200)
    tipo = models.CharField('producto y/o servicio', max_length= 8)
    existencia = models.IntegerField('Existencia',default=0)
    lastChangeDate = models.DateTimeField(auto_now_add = True)
    isActive = models.BooleanField(default=True)