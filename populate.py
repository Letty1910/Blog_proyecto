import os
import django
from random import choice, randint
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post
from accounts.models import Profile
from messaging.models import Message

# Crear superusuario si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')

# Crear usuarios normales
usuarios = []
for i in range(5):
    username = f'user{i}'
    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(username=username, password='testpass')
        print(f"Usuario creado: {username}")
    else:
        user = User.objects.get(username=username)
    usuarios.append(user)

    # Crear perfil si no existe
    profile, created = Profile.objects.get_or_create(user=user)
    profile.biografia = f"Soy {username} y me gusta programar."
    profile.fecha_nacimiento = timezone.now().date().replace(year=1990 + i)
    profile.save()

# Crear posts
titulos = ['Bienvenido', 'Segundo Post', 'Trucos de Django', 'Noticias', 'Tutorial']
for i in range(10):
    Post.objects.create(
        titulo=choice(titulos),
        subtitulo=f'Subtitulo ejemplo {i}',
        contenido=f'<p>Este es el contenido <strong>{i}</strong></p>',
        autor=choice(usuarios)
    )

# Crear mensajes entre usuarios
for i in range(10):
    remitente = choice(usuarios)
    destinatario = choice([u for u in usuarios if u != remitente])
    Message.objects.create(
        remitente=remitente,
        destinatario=destinatario,
        contenido=f'Hola {destinatario.username}, este es un mensaje de prueba #{i}'
    )

print("✔ Usuarios, perfiles, posts y mensajes creados con éxito.")