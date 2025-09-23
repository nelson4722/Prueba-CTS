from celery import shared_task
from django.core.mail import send_mail
from .models import Usuario

@shared_task
def send_verification_email_task(user_id):
    user = Usuario.objects.get(id=user_id)
    send_mail(
        'Verificación de correo',
        f'Enlace: http://localhost:8080/verificar/{user.id}',
        'no-reply@midominio.com',
        [user.email],
    )
    return f'Correo de verificación enviado a {user.email}'