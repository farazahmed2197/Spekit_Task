from folders.models import Folder
from topics.serializers import TopicSerializer
from topics.models import Topic
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.http import Http404

from documents.models import Document

class TopicList(APIView):

    def get(self, request, format=None):
   
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics, many=True)
    
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request, format=None):
        # Create object with serializer along with topics
        data = JSONParser().parse(request)
        serializer = TopicSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        
class TopicsOfObject(APIView):
    
    """
    Returns the topics of provided folder or document name
    """

    def get(self, request, format=None):
        # Get the topic name from query param and retreive the topic object
        folderName = request.GET.get('folder', '')
        documentName = request.GET.get('document', '')
        
        try:
            object_data = ""
            # only provided object one will return, if both provided then it will return the topics of documents
            if not folderName == '':
                object_data = Folder.objects.get(name=folderName)
            if not documentName == '':
                object_data = Document.objects.get(name=documentName)
                
            topics = object_data.topics.all()
            serializer = TopicSerializer(topics, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=201)


class TopicDetail(APIView):
    """
    Retrieve, update or delete a folder instance.
    """
    def get_object(self, pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        folder = self.get_object(pk)
        serializer = TopicSerializer(folder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        topic = self.get_object(pk)
        serializer = TopicSerializer(topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        topic = self.get_object(pk)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


