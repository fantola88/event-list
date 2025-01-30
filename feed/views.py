from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from events.models import Event  # Importa o modelo Event do app 'events'
from chat.models import Message  # Importa o modelo Message do app 'chat'
from chat.forms import MessageForm  # Importa o formulário MessageForm do app 'chat'
from interactions.models import Like

@login_required
def index(request):
    # Pega todos os eventos
    events = Event.get_ranked_events()

    # Pega todas as mensagens ordenadas por timestamp
    messages = Message.objects.all().order_by('timestamp')

    # Verifica quais eventos o usuário atual já curtiu
    liked_event_ids = []
    if request.user.is_authenticated:
        liked_event_ids = Like.objects.filter(user=request.user).values_list('event_id', flat=True)

    # Lógica para enviar mensagens
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Atribui o usuário atual como remetente
            message.save()
            return render(request, 'feed/index.html', {
                'events': events,
                'messages': messages,
                'form': form,
                'liked_event_ids': liked_event_ids,  # Passa a lista de IDs de eventos curtidos
            })
    else:
        form = MessageForm()  # Cria um novo formulário para o caso de não ser POST

    return render(request, 'feed/index.html', {
        'events': events,
        'messages': messages,
        'form': form,
        'liked_event_ids': liked_event_ids,  # Passa a lista de IDs de eventos curtidos
    })
