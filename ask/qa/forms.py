from django.http import Http404
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
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

    def save(self, user):
        question = Question(**self.cleaned_data)
        question.author = user
        question.save()
        return question



class AnswerForm(forms.Form):
    text = forms.CharField(widget = forms.Textarea)
    question = forms.IntegerField()
    question_id = forms.IntegerField()

    def __init__(self,  *args, **kwargs):
        super(AnswerForm, self).__init__(*args,  **kwargs)

    def clean(self):
        cleaned_data = super(AnswerForm, self).clean()
        print "clean",cleaned_data
        return cleaned_data

    def save(self, author):
        print "save",self.cleaned_data
        del self.cleaned_data['question']
        answer = Answer(**self.cleaned_data)
        answer.author = author
        answer.save()
        return answer


class UserCreateForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())
    password1 = forms.CharField(widget = forms.PasswordInput())

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        print 'create',cleaned_data
        password = cleaned_data['password']
        password1 = cleaned_data['password1']
        try:
            user = User.objects.get(username = cleaned_data['username'])
            return None
        except ObjectDoesNotExist:
            pass

        try:
            user = User.objects.get(email = cleaned_data['email'])
            return None
        except ObjectDoesNotExist:
            pass

        if password and password1 and password == password1:
            return cleaned_data
        else:
            return None

    def save(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]
        user = User.objects.create_user(username, email, password)
        user.save()
        return user


