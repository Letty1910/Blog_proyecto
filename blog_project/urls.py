from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import about  # Asegúrate de que la vista 'about' esté en blog/views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),           # URLs para Home y páginas
    path('accounts/', include('accounts.urls')),  # URLs para registro, login, perfil
    path('messaging/', include('messaging.urls')),  # URLs de mensajería
    path('about/', about, name='about'),      # Página "Acerca de mí"
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# Solo en desarrollo: servir archivos MEDIA y STATIC
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)