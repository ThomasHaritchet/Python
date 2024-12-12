# Hato/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'hato/home.html')
