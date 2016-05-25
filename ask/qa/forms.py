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

    def __init__(self, *args, **kwargs):
        self.user,_ = User.objects.get_or_create(
                      username=u'bob',
                      password=u'bobspassword',
                       )
        super(AnswerForm, self).__init__(*args,  **kwargs)

    def clean(self):
        print "clean here"
        logger.debug(self.fields['question'].value())
        logger.debug(self.fields)
        q_id = self.fields['question_id'].value()
        cleaned_data = super(AnswerForm, self).clean()
        print cleaned_data
        logger.debug("answer - clean")
        logger.debug(cleaned_data)
        #q_id = cleaned_data['question']
        #del cleaned_data['question']
        cleaned_data['question_id'] = q_id
        print type(cleaned_data), cleaned_data
        return cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author = self.user
        answer.save()
        return answer





