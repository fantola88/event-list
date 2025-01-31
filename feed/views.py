from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from events.models import Event
from chat.models import Message
from interactions.models import Like
from chat.forms import MessageForm

@login_required
def index(request):
    # Lógica da view
    events = Event.get_ranked_events()
    messages = Message.objects.all().order_by('-timestamp')[:50]
    liked_event_ids = Like.objects.filter(user=request.user).values_list('event_id', flat=True)
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('feed:index')  # Redireciona para evitar reenvio do formulário
    else:
        form = MessageForm()

    return render(request, 'feed/index.html', {
        'events': events,
        'messages': messages,
        'form': form,
        'liked_event_ids': liked_event_ids,
    })