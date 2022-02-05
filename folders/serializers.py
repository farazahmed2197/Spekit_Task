import imp
from rest_framework import serializers
from folders.models import Folder
from topics.models import Topic


class FolderSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    info = serializers.CharField()
    icon = serializers.CharField()
    # topic = serializers.ListField(child=serializers.CharField())
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        print("Data: ", validated_data)
        topic = Topic.objects.get(1)
        data = ""
        
        if topic:
            data = Folder.objects.create(**validated_data)
            
        return data

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.info = validated_data.get('info', instance.info)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance