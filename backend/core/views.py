from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import RegistroSerializer
from .tasks import send_verification_email_task
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
import random

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if Usuario.objects.filter(email=email).exists():
                return Response({"error": "Correo ya inscrito"}, status=400)
            user = serializer.save()
            send_verification_email_task.delay(user.id)
            return Response({"mensaje": "Registro exitoso"})
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def verificar_correo(request):
    user_id = request.data.get("id")
    user = Usuario.objects.filter(id=user_id).first()
    if user:
        user.verificado = True
        user.save()
        return Response({"mensaje": "Correo verificado correctamente"})
    return Response({"error": "Usuario no encontrado"}, status=404)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def generar_ganador(request):
    concursantes = Usuario.objects.filter(verificado=True, ganador=False)
    if concursantes:
        ganador = random.choice(list(concursantes))
        ganador.ganador = True
        ganador.save()
        return Response({"ganador": ganador.username, "correo": ganador.email})
    return Response({"error": "No hay concursantes válidos"}, status=404)
