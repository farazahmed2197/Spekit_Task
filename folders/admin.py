from django.contrib import admin
from .models import Folder, FolderTopic

# Register your models here.

admin.site.register((Folder))
admin.site.register((FolderTopic))