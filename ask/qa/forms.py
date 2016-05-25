from django import forms
from django.contrib.auth.models import User
from .models import Question, Answer

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
    question_id = forms.IntegerField()

    def clean(self):
        print "clean here"
        cleaned_data = super(AnswerForm, self).clean()
        return cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        user,_ = User.objects.get_or_create(
                username=u'bob',
                password=u'bobspassword',
                    )
        answer.author = user
        answer.save()
        return answer





