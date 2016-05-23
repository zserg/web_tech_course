from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse

from .models import Question, Answer

@require_GET
def question_details(request, slug):
    question = get_object_or_404(Question, id = slug)
    try:
       answers = Answer.objects.filter(question = question)
    except Answer.DoesNotExist:
        answers = None

    return render(request, 'qa/question_details.html',
                  {'question' : question,
                   'answers' : answers})


