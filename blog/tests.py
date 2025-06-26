from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post
from django.core.files.uploadedfile import SimpleUploadedFile

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='autor', password='testpass')
        self.post = Post.objects.create(
            titulo='Título de prueba',
            subtitulo='Subtítulo',
            contenido='Contenido del post',
            imagen=SimpleUploadedFile(name='test.jpg', content=b'', content_type='image/jpeg'),
            autor=self.user
        )

    def test_post_str(self):
        self.assertEqual(str(self.post), 'Título de prueba')

    def test_post_fields(self):
        self.assertEqual(self.post.autor.username, 'autor')
        self.assertTrue(self.post.fecha)

class PostViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='autor', password='testpass')
        self.post = Post.objects.create(
            titulo='Post para test',
            subtitulo='Subtítulo',
            contenido='Contenido...',
            imagen=SimpleUploadedFile(name='test.jpg', content=b'', content_type='image/jpeg'),
            autor=self.user
        )

    def test_home_view_status(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post para test')

    def test_post_detail_view(self):
        response = self.client.get(reverse('page_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contenido...')

    def test_create_view_requires_login(self):
        response = self.client.get(reverse('page_create'))
        self.assertRedirects(response, f"/accounts/login/?next=/pages/create/")

    def test_create_post_logged_in(self):
        self.client.login(username='autor', password='testpass')
        response = self.client.post(reverse('page_create'), {
            'titulo': 'Nuevo Post',
            'subtitulo': 'Sub',
            'contenido': 'Contenido nuevo',
            'imagen': SimpleUploadedFile(name='nuevo.jpg', content=b'', content_type='image/jpeg'),
        })
        self.assertEqual(Post.objects.last().titulo, 'Nuevo Post')