from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('noteslist',views.NotesListView.as_view(),name='noteslist'),
    path('notes/<int:pk>',views.NoteDetailView.as_view())
    ]