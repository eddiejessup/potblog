from datetime import datetime
# from google.appengine.ext import ndb
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateField(default=timezone.now)
    text = models.CharField(max_length=4000)

    def __str__(self):
        return self.title

    def num_comments(self):
        return Comment.objects.filter(post__pk=self.pk).count()


class Comment(models.Model):
    post = models.ForeignKey('Post')
    author = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    time_published = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
    is_hidden = models.BooleanField(default=False)
