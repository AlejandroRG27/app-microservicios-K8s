from django.db import models
import uuid

class Tarea (models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=600)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_uuid = models.UUIDField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre