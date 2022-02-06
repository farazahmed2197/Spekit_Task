from django.db import models
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=30, unique=True)
    short_description = models.CharField(max_length=240)
    long_description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    