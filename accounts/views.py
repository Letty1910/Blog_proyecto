# accounts/views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserRegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile_view.html', {'profile': profile})

@login_required
def profile_edit(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu perfil se actualizó correctamente.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # 1) Creo el User
            # 2) Creo el Profile *solo una vez* aquí
            Profile.objects.create(
                user=user,
                avatar=form.cleaned_data.get('avatar'),
                biografia=form.cleaned_data.get('biografia'),
                fecha_nacimiento=form.cleaned_data.get('fecha_nacimiento')
            )
            messages.success(request,
                "¡Tu cuenta ha sido creada! Ya podés iniciar sesión.")
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html')