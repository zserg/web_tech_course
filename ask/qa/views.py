from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question, Answer
from .forms import AnswerForm, AskForm
import logging

logger = logging.getLogger('APPNAME')

def question_details(request, slug):
    logger.debug('Logging here')

    if request.method == 'POST':
        logger.debug('cp0')
        logger.debug(request.POST)
        print 'Hello', request.POST
        print 'id', request.POST['question']

        form = AnswerForm(request.POST)
        if form.is_valid():
            print "Yes"
            print 'Cleaned', form.cleaned_data
            answer = form.save()
            url = reverse('question-details', args=(form.cleaned_data['question_id'],))
            return HttpResponseRedirect(url)

    logger.debug('cp1')
    logger.debug(request.GET)
    que = get_object_or_404(Question, id = slug)
    try:
       answers = Answer.objects.filter(question = que)
    except Answer.DoesNotExist:
        answers = None
    form = AnswerForm(initial = {'question':slug})
    return render(request, 'qa/question_details.html',
                  {'question' : que,
                   'answers' : answers,
                   'form' : form}
                  )


def ask(request):
    logger.debug('Logging here ask')
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html',
                      {'form' : form})


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




