from django.urls import path
from django.contrib.auth.views import LoginView
from blog.views import LogoutGETView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', LogoutGETView.as_view(next_page='home'), name='logout'),
]