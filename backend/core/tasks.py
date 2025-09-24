from django.core.mail import send_mail
from django.conf import settings
from prueba_cts.celery import app


@app.task
def send_verification_email(user_id, email):
    verification_link = f"http://localhost:3000/verificar?id={user_id}"
    send_mail(
        'Verifica tu correo',
        f'Para verificar tu cuenta haz click aquí: {verification_link}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
