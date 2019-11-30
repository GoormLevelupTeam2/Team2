from django.urls import path
from .views import *

urlpatterns = [
    path('select/', select, name='select'),
    path('hangman/', hangman, name='hangman'),
    path('quiz/<int:pk>/', quiz, name='quiz'),
]
