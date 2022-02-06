from folders.models import Folder
from folders.serializers import FolderSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import JsonResponse
from django.http import Http404

from documents.models import Document

class FolderList(APIView):

    def get(self, request, format=None):
   
        folders = Folder.objects.all()
        serializer = FolderSerializer(folders, many=True)
    
        return JsonResponse(serializer.data, safe=False, status=200)

    def post(self, request, format=None):
        # Create object with serializer along with topics
        data = JSONParser().parse(request)
        serializer = FolderSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

class TopicFolderList(APIView):
    
    """
    Returns the folders of provided topic name
    """

    def get(self, request, format=None):
        # Get the topic name from query param and retreive the topic object
        topicName = request.GET.get('topic', '')
        try:
        
            folders = Folder.objects.filter(topics__name = topicName)
            serializer = FolderSerializer(folders, many=True)
        
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=201)

class FolderDetail(APIView):
    """
    Retrieve, update or delete a folder instance.
    """
    def get_object(self, pk):
        try:
            return Folder.objects.get(pk=pk)
        except Folder.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        folder = self.get_object(pk)
        serializer = FolderSerializer(folder, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        folder = self.get_object(pk)
        folder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
