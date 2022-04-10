from django import views
from django.urls import path
from . import views
urlpatterns=[
    path('noteslist',views.noteslist,name='noteslist'),
    path('notes/<int:pk>',views.detail)
    ]