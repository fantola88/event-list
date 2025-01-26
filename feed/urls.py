from django.urls import path
from feed.views import index 

urlpatterns = [
    path('', index),
]