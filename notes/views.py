from django.shortcuts import render

from .models import Note

def list_notes(request):
    all_notes = Note.objects.all
    return render(request, 'notes/notes_list.html', {'notes': all_notes})