from django.db import models
from folders.models import Folder
from django.utils import timezone

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    size = models.CharField(max_length=30),
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
