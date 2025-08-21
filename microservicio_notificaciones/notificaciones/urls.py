from django.urls import path
from .views import Notificar, NotificacionList

urlpatterns = [
    path('notificar/<uuid:uuid>/', Notificar.as_view()),
    path('notificaciones/', NotificacionList.as_view()),
]