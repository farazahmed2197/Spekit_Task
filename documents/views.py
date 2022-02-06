from .serializers import DocumentSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404

from documents.models import Document


class DocumentList(APIView):

    def get(self, request, format=None):
        
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request, format=None):
        # Create object with serializer along with topics
        data = JSONParser().parse(request)
        serializer = DocumentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

class TopicDocumentList(APIView):
    
    """
    Returns the documents of provided topic name and folder name
    """

    def get(self, request, format=None):
        # Get the topic name from query param and retreive the topic object
        topicName = request.GET.get('topic', '')
        folderName = request.GET.get('folder', '')
        
        kwargs = {}
        
        try:
            # prepare arguments for query
            if topicName != '':
                kwargs['topics__name'] = topicName
            
            if folderName != '':
                kwargs['folder__name'] = folderName
                
            documents = Document.objects.filter(**kwargs)
            # Serialize the data
            serializer = DocumentSerializer(documents, many=True)
        
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=201)

class DocumentDetail(APIView):
    """
    Retrieve, update or delete a document instance.
    """
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
