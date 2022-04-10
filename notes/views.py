from pyexpat import model
from re import S, template
from urllib.request import Request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Notes
from .forms import NotesForm
from django.views.generic import DetailView,ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NotesCreateView(CreateView):
    model=Notes
    form_class=NotesForm
    success_url='/notes/noteslist/'

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()

        return HttpResponseRedirect(self.success_url)


class NotesUpdateView(UpdateView):
    model=Notes
    form_class=NotesForm
    success_url='/notes/noteslist/'


class NotesDeleteView(DeleteView):
    model=Notes
    template_name='notes/notes_delete.html'
    success_url='/notes/noteslist/'

class NotesListView(LoginRequiredMixin,ListView):
    model=Notes
    context_object_name="notes"
    template_name='notes/noteslist.html'
    login_url='login'

    #overriding the original method of listview
    def get_queryset(self) :
        return self.request.user.notes.all()

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