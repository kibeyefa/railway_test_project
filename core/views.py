from django.shortcuts import redirect, render
from .models import Note
from django.views.generic import ListView
from django.http import HttpResponse


# Create your views here.
def index(request):
    notes = Note.objects.all()
    template = 'cores/index.html'
    context = dict(notes=notes, notes_count=notes.count())

    return render(request, template_name=template, context=context)
    return HttpResponse('Hello world')


class NoteListView(ListView):
    template_name = 'cores/index.html'
    queryset = Note.objects.all()


def viewNote(request, pk):
    note = Note.objects.get(id=pk)
    template = 'cores/note.html'
    context = {'note': note}
    # print(note.data)

    if request.method == 'POST':
        # print(request.POST['note'])
        if request.POST['note'] == '':
            note.delete()
            return redirect('index')
        else:
            note.note = request.POST['note']
            note.save()
            return redirect('index')

    return render(request, template, context)


def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('index')


def addNote(request):
    template = 'cores/add.html'

    if request.method == 'POST':
        if request.POST['note'] == '':
            return redirect('index')
        else:
            note_data = request.POST['note']
            note = Note.objects.create(note=note_data)
            return redirect('index')

    return render(request, template)
