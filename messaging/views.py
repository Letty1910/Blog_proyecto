# MENSAJERÍA (messaging/views.py)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.contrib.auth.models import User

@login_required
def inbox(request):
    mensajes = Message.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'messaging/inbox.html', {'mensajes': mensajes})

@login_required
def send_message(request, username):
    destinatario = get_object_or_404(User, username=username)
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            Message.objects.create(remitente=request.user, destinatario=destinatario, contenido=contenido)
            return redirect('inbox')
    return render(request, 'messaging/send_message.html', {'destinatario': destinatario})