from django.shortcuts import render
from .models import Question
from .forms import AnswerInputForm


def hangman(request):
    pass


def quiz(request, pk):
    question = Question.objects.filter(id=pk)
    correct = 't'

    for q in question:
        pass

    if request.method == 'POST':
        form = AnswerInputForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['input'] == q.answer:
                correct = True
            else:
                correct = False

        else:
            print('error!!!')
    else:
        form = AnswerInputForm()

    return render(request, 'game/game.html', {
        'question': question,
        'form': form,
        'correct': correct,
    })
>>>>>>> game
