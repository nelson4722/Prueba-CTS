from django.test import TestCase
from .models import Usuario

class UsuarioTestCase(TestCase):
    def test_creacion_usuario(self):
        user = Usuario.objects.create_user(username="test", email="test@test.cl", telefono="123456789", password="pass")
        self.assertEqual(user.email, "test@test.cl")
        self.assertFalse(user.verificado)
        self.assertFalse(user.ganador)
        self.assertEqual(user.puntos, 0)