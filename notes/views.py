from django.shortcuts import render
from django.http import Http404

from .models import Note

def list_notes(request):
    all_notes = Note.objects.all
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail_note(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'notes/note_details.html', {'note': note})