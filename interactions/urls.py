# interactions/urls.py
from django.urls import path
from .views import like_event

app_name = 'interactions'

urlpatterns = [
    path('like/<int:event_id>/', like_event, name='like_event'),
]