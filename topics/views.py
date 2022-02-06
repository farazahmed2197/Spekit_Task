from django.shortcuts import render

# Create your views here.

class AllTopicsOfFolder(APIView):
    
    """
    Returns the topics of provided folder name
    """

    def get(self, request, format=None):
        # Get the topic name from query param and retreive the topic object
        folderName = request.GET.get('name', '')
        
        try:
            folder_data = Folder.objects.get(name=folderName)
            topics = folder_data.topics.all()       
            data = serializers.serialize('json', topics)
            return HttpResponse(data)
        except Exception as e:
            print(e)
            return JsonResponse([], safe=False, status=201)