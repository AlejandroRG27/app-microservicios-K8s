from django.db import models
import uuid

class Usuario(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
