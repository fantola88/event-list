# interactions/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from events.models import Event
from .models import Like

@login_required
def like_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Verifica se o usuário já curtiu o evento
    like, created = Like.objects.get_or_create(user=request.user, event=event)
    if not created:
        like.delete()  # Remove a curtida se já existir (funcionalidade de "descurtir")
    return redirect('index')  # Redireciona para a página inicial ou outra URL