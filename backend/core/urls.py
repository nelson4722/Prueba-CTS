from django.urls import path
from .views import RegistroView, verificar_correo, generar_ganador

urlpatterns = [
    path('registro/', RegistroView.as_view()),
    path('verificar-correo/', verificar_correo),
    path('generar-ganador/', generar_ganador),
]
    # --- IGNORE ---   