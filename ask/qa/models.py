from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
   def new(self):
      pass

   def popular(self):
      pass


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now = True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, related_name = 'question_author')
    likes = models.ManyToManyField(User, related_name = 'question_likes', blank = True)
    objects = QuestionManager()

    def get_url(self):
        url = reverse('question-details', args=(self.pk,))
        return url

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now = True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)


# class User(models.Models):
#     login = model.CharField(unique=true)
#     password = model.CharField()
#     name = model.CharField()

# class Session(models.Models):
#     key = model.CharField(unique=true)
#     user = model.ForeignKey(User)
#     expires = model.DateTimeField()
