from statistics import mode
from django.db import models
from django.utils import timezone

from topics.models import Topic

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=30, unique=True)
    info = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    topics = models.ManyToManyField(Topic, through='FolderTopic')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class FolderTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)