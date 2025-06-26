from django.urls import path
from .views import HomeView, PostDetail, PostCreate, PostUpdate, PostDelete, about

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', about, name='about'),  # Ruta para la vista "about"
    path('pages/', HomeView.as_view(), name='pages'),
    path('pages/create/', PostCreate.as_view(), name='page_create'),
    path('pages/<int:pk>/', PostDetail.as_view(), name='page_detail'),
    path('pages/<int:pk>/edit/', PostUpdate.as_view(), name='page_edit'),
    path('pages/<int:pk>/delete/', PostDelete.as_view(), name='page_delete'),
]