from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Message
from django.urls import reverse

class MessageModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='remitente', password='12345')
        self.user2 = User.objects.create_user(username='destinatario', password='12345')
        self.message = Message.objects.create(
            remitente=self.user1,
            destinatario=self.user2,
            contenido='Hola, este es un mensaje de prueba.'
        )

    def test_message_creation(self):
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(self.message.remitente.username, 'remitente')
        self.assertEqual(self.message.destinatario.username, 'destinatario')
        self.assertFalse(self.message.leido)

    def test_message_str(self):
        expected_str = f'De remitente a destinatario - {self.message.fecha_envio.strftime("%d/%m/%Y %H:%M")}'
        self.assertEqual(str(self.message), expected_str)

class InboxViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='remitente', password='12345')
        self.user2 = User.objects.create_user(username='destinatario', password='12345')
        Message.objects.create(
            remitente=self.user1,
            destinatario=self.user2,
            contenido='Mensaje para la bandeja de entrada.'
        )
        self.client = Client()
        self.client.login(username='destinatario', password='12345')

    def test_inbox_view(self):
        response = self.client.get(reverse('inbox'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Mensaje para la bandeja de entrada.')