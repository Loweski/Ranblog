from django.db import models

from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100)
    created_date = models.DateTimeField('date added')

    def __str__(self):
        return self.topic_name

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField('date created')
    strip = False

    def __str__(self):
        return self.title
