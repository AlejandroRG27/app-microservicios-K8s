from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class TareaList(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    
class TareaDetalle(APIView):
    def get(self, request, uuid):
        try:
            tarea = Tarea.objects.get(uuid=uuid)
            tarea_data = TareaSerializer(tarea).data
            
            if tarea.usuario_uuid:
                # Consulta API de usuarios
                response = requests.get(f"http://usuarios:8001/api/usuarios/?uuid={tarea.usuario_uuid}")
                if response.status_code == 200:
                    usuarios = response.json()
                    if usuarios:  # Asume que filtra por uuid en el futuro; por ahora lista
                        tarea_data['usuario_detalle'] = usuarios[0]  # Simplificado
            
            return Response(tarea_data)
        except Tarea.DoesNotExist:
            return Response({"error": "Tarea no encontrada"}, status=404)