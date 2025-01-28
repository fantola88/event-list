from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
# Create your views here.

@login_required
def index(request):
    user = get_user(request)
    print(f"Usuário logado: {user}")  # Isso vai aparecer no terminal
    return render(request, 'feed/index.html')