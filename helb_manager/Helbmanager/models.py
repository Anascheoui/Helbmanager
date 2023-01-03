from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=100)#create a title of max 100 caracter
    content = models.TextField()# the content is suposed to be a text
    date_posted = models.DateTimeField(default=timezone.now)#this show the date when the post was posted no parentheses cause don t need to call the function
    author = models.ForeignKey(User, on_delete=models.CASCADE)# if user is deleted his post will be deleted too

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class CreateProject(models.Model):
    name = models.CharField(max_length=128, unique=True)
    users = models.ManyToManyField(User, related_name='collaborater')

    class Meta:
        ordering = ['name']




