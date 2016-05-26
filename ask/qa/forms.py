from django.http import Http404
from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer
import logging

logger = logging.getLogger('APPNAME')

class AskForm(forms.Form):
    title = forms.CharField(max_length = 255)
    text = forms.CharField(widget = forms.Textarea)

    def clean(self):
        print "clean here"
        cleaned_data = super(AskForm, self).clean()
        return cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        user,_ = User.objects.get_or_create(
                username=u'bob',
                password=u'bobspassword',
                    )
        question.author = user
        question.save()
        return question



class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.IntegerField()
    question_id = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        self.user,_ = User.objects.get_or_create(
                      username=u'bob',
                      password=u'bobspassword',
                       )
        super(AnswerForm, self).__init__(*args,  **kwargs)

    def clean(self):
        cleaned_data = super(AnswerForm, self).clean()
        print "clean",cleaned_data
        return cleaned_data

    def save(self):
        print "save",self.cleaned_data
        del self.cleaned_data['question']
        answer = Answer(**self.cleaned_data)
        answer.author = self.user
        answer.save()
        return answer





