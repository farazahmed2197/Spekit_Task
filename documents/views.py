from folders.models import Folder, FolderTopic
from .serializers import DocumentSerializer
from topics.models import Topic
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse

from documents.models import Document


class DocumentList(APIView):

    def get(self, request, format=None):
        
        folder_topic = FolderTopic.objects.filter()
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        folder = Folder.objects.get(name="client feedback1")
        topic = Topic.objects.get(name="policy")
        
        folder_topic = folder.topics.all()
        
        document_data = Document.objects.filter(folder=folder, topics__name ="policy")
        
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
    Returns the documents of provided topic name
    """

    def get(self, request, format=None):
        # Get the topic name from query param and retreive the topic object
        topicName = request.GET.get('topic', '')
        folderName = request.GET.get('folder', '')
        
        try:
            documents = ""
            if folderName == "":
                documents = Document.objects.filter(topics__name = topicName)
            else:
                documents = Document.objects.filter(folder__name=folderName, topics__name = topicName)
                
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
