from django.urls import path
from .views import *

urlpatterns = [
    path('hangman/', quiz, name='quiz'),
    path('quiz', hangman, name='hangman'),
]
