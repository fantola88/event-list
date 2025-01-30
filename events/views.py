# views.py
from django.shortcuts import render, redirect
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from .models import Event

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)  # Não salva automaticamente
            event.creator = request.user  # Define o criador do evento como o usuário logado
            event.save()
            return redirect('index')  # Redireciona para a página inicial após o cadastro
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})

