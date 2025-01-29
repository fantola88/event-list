from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def chat_view(request):
    messages = Message.objects.all().order_by('timestamp')  # Exibe todas as mensagens ordenadas por data
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user  # Atribui o usuário atual como remetente
            message.save()
            return redirect('chat')  # Redireciona de volta para o chat
    else:
        form = MessageForm()
    
    return render(request, 'chat/chat_view.html', {'messages': messages, 'form': form})
