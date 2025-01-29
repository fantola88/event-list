from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
from events.models import Event  # Importa o modelo Event do app 'events'

# Create your views here.

@login_required
def index(request):
    events = Event.objects.all()
    return render(request, 'feed/index.html', {'events': events})