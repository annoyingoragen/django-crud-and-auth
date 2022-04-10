from urllib.request import Request
from django.shortcuts import render

import notes
from .models import Notes
from django.views.generic import DetailView,ListView
# Create your views here.

class NotesListView(ListView):
    model=Notes
    context_object_name="notes"
    template_name='notes/noteslist.html'



# def noteslist(request):
#     notes=Notes.objects.all()
#     return render(request,'notes/noteslist.html',{'notes':notes})


class NoteDetailView(DetailView):
    model=Notes
    context_object_name="note"
    template_name='notes/detail.html'


# def detail(request,pk):
#       note=Notes.objects.get(pk=pk)
#       return render(request,'notes/detail.html',{'note':note})