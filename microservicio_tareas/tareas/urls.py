from django.urls import path
from .views import TareaList, TareaDetalle

urlpatterns = [
    path('tareas/', TareaList.as_view()),
    path('tareas/<uuid:uuid>/', TareaDetalle.as_view()),
]