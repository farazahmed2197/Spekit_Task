from rest_framework import serializers
from folders.models import Folder


class FolderSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    info = serializers.CharField()
    icon = serializers.CharField()
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    topics = serializers.ListField(write_only=True, child=serializers.IntegerField(min_value=0))
    
    def create(self, validated_data):
        print("Data: ", validated_data)
        
        data = Folder.objects.create(name = validated_data["name"], info=validated_data["info"], icon=validated_data["icon"])
        data.topics.set(validated_data["topics"])
        
        return data

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.info = validated_data.get('info', instance.info)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.save()
        return instance