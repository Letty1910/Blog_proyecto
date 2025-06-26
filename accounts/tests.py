from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_profile_creation(self):
        profile = Profile.objects.create(user=self.user, biografia="Bio de prueba")
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(str(profile), f"Perfil de {self.user.username}")

class ProfileFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'biografia': 'Una biografía corta.',
            'fecha_nacimiento': '2000-01-01',
        }
        form = ProfileForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ProfileForm(data={})
        self.assertTrue(form.is_valid())  # Aún válido porque todos los campos son opcionales

class ProfileViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='usuario', password='12345')
        self.client.login(username='usuario', password='12345')

    def test_profile_view_get(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile_view.html')

    def test_profile_edit_get(self):
        response = self.client.get(reverse('profile_edit'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile_edit.html')

    def test_profile_edit_post(self):
        response = self.client.post(reverse('profile_edit'), {
            'biografia': 'Editando perfil',
            'fecha_nacimiento': '1990-01-01',
        })
        self.assertRedirects(response, reverse('profile'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.profile.biografia, 'Editando perfil')