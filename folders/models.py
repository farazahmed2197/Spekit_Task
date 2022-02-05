from django.db import models
from django.utils import timezone

# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=30)
    info = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
