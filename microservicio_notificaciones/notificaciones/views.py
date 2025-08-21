from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from datetime import datetime
from rest_framework import generics
from .serializers import NotificacionSerializer
from .models import Notificaciones

class Notificar(APIView):
    def post(self, request, uuid):
        # Consulta microservicio de tareas
        tarea_response = requests.get(f"http://tareas:8000/api/tareas/{uuid}/")
        if tarea_response.status_code != 200:
            return Response({"error": "Tarea no encontrada"}, status=404)
        
        tarea_data = tarea_response.json()
        if not tarea_data.get('completada'):
            return Response({"mensaje": "Tarea no completada, no se envía notificación"})
        
        # Obtiene email de usuario (asumiendo tarea_data tiene 'usuario_detalle' con email)
        email = tarea_data.get('usuario_detalle', {}).get('email', 'desconocido')
        
        # Simula envío: Log y guarda en DB
        mensaje = f"Notificación enviada a {email}: Tarea {uuid} completada!"
        print(mensaje)  # Simulación de email/log
        Notificaciones.objects.create(tarea_uuid=uuid, mensaje=mensaje)
        
        return Response({"mensaje": mensaje, "enviada": True})

class NotificacionList(generics.ListAPIView):  # Opcional: Lista logs
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionSerializer