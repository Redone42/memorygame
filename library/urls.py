# urls.py (inside your app)
from django.urls import path
from . import views

urlpatterns = [
    path('game/', views.memory_game, name='memory_game'),  # Updated path
]
