from urllib.request import Request
from django.shortcuts import render
from .models import Notes
# Create your views here.

def noteslist(request):
    notes=Notes.objects.all()
    return render(request,'notes/noteslist.html',{'notes':notes})

def detail(request,pk):
      note=Notes.objects.get(pk=pk)
      return render(request,'notes/detail.html',{'note':note})