# views.py
from django.shortcuts import render

def memory_game(request):
    return render(request, 'memory.html')
