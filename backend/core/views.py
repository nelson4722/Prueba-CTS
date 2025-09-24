from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuario
from .serializers import RegistroSerializer
from .tasks import send_verification_email
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
import random

class RegistroView(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if Usuario.objects.filter(email=email).exists():
                return Response({"error": "Correo ya inscrito"}, status=400)
            user = serializer.save()
            print(user.id)
            send_verification_email.delay(user.id, email)
            return Response({"mensaje": "Registro exitoso "+str(user.id)})
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

@csrf_exempt
@api_view(['POST'])
def generar_ganador(request):
    concursantes = Usuario.objects.filter(verificado=True, ganador=False)
    print(Usuario)
    if concursantes:
        ganador = random.choice(list(concursantes))
        ganador.ganador = True
        ganador.save()
        return Response({"ganador": ganador.username, "correo": ganador.email})
    return Response({"error": "No hay concursantes válidos"}, status=404)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username == "admin" and password == "adminpass":
            return Response({"mensaje": "Login exitoso"})
        else:
            return Response({"error": "Credenciales inválidas"}, status=400)
