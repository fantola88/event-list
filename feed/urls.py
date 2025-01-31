from django.urls import path
from . import views

app_name = 'feed'  # Namespace do app

urlpatterns = [
    path('', views.index, name='index'),  # URL raiz para a página inicial
]