from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
                   'answers' : answers}
                  )


@require_GET
def question_list(request):
    question_list = Question.objects.all().order_by('-added_at')
    paginator = Paginator(question_list, 10)

    page = request.GET.get('page')
    try:
       questions = paginator.page(page)
    except PageNotAnInteger:
       questions = paginator.page(1)
    except EmptyPage:
       questions = paginator.page(paginator.num_pages)

    return render(request, 'qa/question_list.html',
                  {'questions' : questions}
                  )


@require_GET
def popular_list(request):
    popular_list = Question.objects.all().order_by('-rating')
    paginator = Paginator(popular_list, 10)

    page = request.GET.get('page')
    try:
       pquestions = paginator.page(page)
    except PageNotAnInteger:
       pquestions = paginator.page(1)
    except EmptyPage:
       pquestions = paginator.page(paginator.num_pages)

    return render(request, 'qa/popular_list.html',
                  {'pquestions' : pquestions}
                  )




