from rest_framework import serializers
from .models import Notificaciones

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'