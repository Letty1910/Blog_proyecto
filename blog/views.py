# VISTAS BASADAS EN CLASE + MIXIN (blog/views.py)
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'post_form.html'
    success_url = '/pages/'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'post_form.html'
    success_url = '/pages/'

class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = '/pages/'

class LogoutGETView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
def about(request):
    return render(request, 'about.html')