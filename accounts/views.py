# VISTAS DE PERFIL (accounts/views.py)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile
from .forms import Profile
from .forms import UserRegisterForm

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile_view.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = Profile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = Profile(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.avatar = form.cleaned_data.get('avatar')
            profile.biografia = form.cleaned_data.get('biografia')
            profile.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
            profile.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})