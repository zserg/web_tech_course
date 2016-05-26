from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Question, Answer
from .forms import AnswerForm, AskForm
import logging

logger = logging.getLogger('APPNAME')

@login_required
def question_details(request, slug):
    logger.debug('Logging here')

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username = request.user.username)
            answer = form.save(user)
            url = reverse('question-details', args=(form.cleaned_data['question_id'],))
            return HttpResponseRedirect(url)

    que = get_object_or_404(Question, id = slug)
    try:
       answers = Answer.objects.filter(question = que)
    except Answer.DoesNotExist:
        answers = None
    form = AnswerForm(initial = {'question_id':slug, 'question':slug})
    return render(request, 'qa/question_details.html',
                  {'question' : que,
                   'answers' : answers,
                   'form' : form}
                  )


@login_required
def ask(request):
    logger.debug('Logging here ask')
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username = request.user.username)
            question = form.save(user)
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        user = request.user.username
    return render(request, 'qa/ask.html',
            {'form' : form, 'user': user})


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

    user = request.user.username
    return render(request, 'qa/question_list.html',
                  {'questions' : questions, 'user': user}
                  )


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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            url = reverse('question-list')
            return HttpResponseRedirect(url)
    else:
        form = UserCreationForm()

    return render(request, 'qa/signup.html',
                 {'form': form})




