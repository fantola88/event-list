from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from events.models import Event  # Importa o modelo Event do app 'events'
from chat.models import Message  # Importa o modelo Message do app 'chat'
from chat.forms import MessageForm  # Importa o formulário MessageForm do app 'chat'

@login_required
def index(request):
    events = Event.objects.all()  # Pega todos os eventos
    messages = Message.objects.all().order_by('timestamp')  # Pega todas as mensagens ordenadas
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Atribui o usuário atual como remetente
            message.save()
            return render(request, 'feed/index.html', {'events': events, 'messages': messages, 'form': form})
    else:
        form = MessageForm()  # Cria um novo formulário para o caso de não ser POST
    
    return render(request, 'feed/index.html', {'events': events, 'messages': messages, 'form': form})
