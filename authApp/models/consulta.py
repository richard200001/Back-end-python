from django.db import models
from .usuario import Usuario
from .inventario import Inventario 

class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    idUsu = models.ForeignKey(Usuario, related_name='consulta', on_delete=models.CASCADE)
    idInv = models.ForeignKey(Inventario, related_name='consulta', on_delete=models.CASCADE)
    registro = models.DateTimeField(auto_now_add = True)
    