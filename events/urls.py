# urls.py
from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('create/', views.create_event, name='create_event'),  # URL para criar evento
    path('search/', views.search_events, name='search_events'),  # Outras URLs   
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # Detalhes do evento
]