# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    avatar = forms.ImageField(required=False)
    biografia = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'avatar', 'biografia', 'fecha_nacimiento']