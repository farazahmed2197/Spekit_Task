from documents.models import Document
from rest_framework import viewsets
from rest_framework import permissions
from documents.serializers import DocumetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows documents to be viewed or edited.
    """
    queryset = Document.objects.all().order_by('name')
    serializer_class = DocumetSerializer
    permission_classes = [permissions.IsAuthenticated]