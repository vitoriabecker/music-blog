from django.conf import settings
from django.db import models
from django.utils import timezone

class Song(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=100)
  songwriter =  models.CharField(max_length=200)
  year = models.TextField(max_length=4, blank=True, null=True)
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now
    self.save()

  def __str__(self):
    return self.title

