from django.contrib import admin
from .models import Document, DocumentTopic
# Register your models here.

admin.site.register((Document))
admin.site.register((DocumentTopic))