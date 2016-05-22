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
    likes = models.ManyToManyField(User, related_name = 'question_likes')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)

