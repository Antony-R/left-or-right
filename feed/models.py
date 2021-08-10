from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
    left_title = models.CharField(max_length=200, default='')
    left_content = models.CharField(max_length=200, default='')
    left_vote = models.ManyToManyField(User, blank=True, related_name='left_vote')
    right_title = models.CharField(max_length=200, default='')
    right_content = models.CharField(max_length=200, default='')
    right_vote = models.ManyToManyField(User, blank=True, related_name='right_vote')

    def __str__(self) -> str:
        return self.title

