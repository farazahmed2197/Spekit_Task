import imp
from unicodedata import name
from django.shortcuts import render
from folders.models import Folder, FolderTopic
from folders.serializers import FolderSerializer
from topics.models import Topic
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from documents.models import Document

# Create your views here.
@csrf_exempt
def folder_list(request):
    """
    List all code folders, or create a new folder.
    """
    if request.method == 'GET':
        folder_topic = FolderTopic.objects.filter()
        folders = Folder.objects.values()
        # serializer = FolderSerializer(folders, many=True)
        folder = Folder.objects.get(name="default")
        topic = Topic.objects.get(name="policy")
        
        folder_topic = folder.topics.all()
        
        Document.objects.filter()
        jData = list(folders)
        folderTopicData = serializers.serialize('json', folder_topic)
        return JsonResponse(folderTopicData, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FolderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def folder_detail(request, pk):
    """
    Retrieve, update or delete a code folder.
    """
    try:
        folder = Folder.objects.get(pk=pk)
    except Folder.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = FolderSerializer(folder)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FolderSerializer(folder, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        folder.delete()
        return HttpResponse(status=204)
    
    
# @api_view(['POST'])
# def forget_password_view(request):
#     data = {}
#     try:
#         if request.method == 'POST':
#             serializer = ForgetPasswordSerializer(data=request.data)
#             if serializer.is_valid():
#                 email = request.data['email']
#                 try:
#                     user = User.objects.get(email=email, is_deleted=0)
#                 except Exception as e:
#                     data['status'] = -2
#                     data['developer_message'] = "Invalid Email Address"
#                     return JsonResponse(data, status=http.HTTPStatus.UNAUTHORIZED)