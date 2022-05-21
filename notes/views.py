from django.shortcuts import render
from .models import Note

def list_views(request):
    notes = Note.objects.all()
    context = {
        'list_views': notes,
    }
    return render(request, 'home.html', context)
