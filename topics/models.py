from tkinter import CASCADE
from django.db import models
from folders.models import Folder
from documents.models import Document
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=240)
    long_description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
class FolderTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

class DocumentTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)