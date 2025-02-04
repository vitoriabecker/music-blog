from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Song(models.Model):
  artist = models.CharField(max_length=200)
  title = models.CharField(max_length=100)
  year = models.TextField(max_length=4, blank=True, null=True)

  def __str__(self):
    return self.title
  
  def number_of_comments(self):
    return Comment.objects.filter(song=self).count()
  
  
class Comment(models.Model):
  song = models.ForeignKey(Song, related_name='comments', on_delete=models.CASCADE)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  content = models.TextField(max_length=450)
  created_date = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ['created_date',]

  def __str__(self):
    return "Comment {} by {}".format(self.content, self.user)

