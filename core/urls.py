from os import name
from core.views import NoteListView, addNote, deleteNote, index, viewNote
from django.urls import path
from .urls import *

urlpatterns = [
    path('', index, name='index'),
    # path('', NoteListView.as_view(), name='index'),
    path('add/', addNote),
    path('note/<str:pk>/', viewNote, name='note'),
    path('delete/<str:pk>/', deleteNote)
]
