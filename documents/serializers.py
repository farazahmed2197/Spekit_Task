from documents.models import Document
from rest_framework import serializers


class DocumetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ['name', 'topic', 'type', 'size']