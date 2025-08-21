from django.db import models
import uuid

class Notificaciones(models.Model):
    tarea_uuid = models.UUIDField()
    mensaje = models.TextField()
    enviada_en = models.DateTimeField(auto_now_add=True)
