from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    type = serializers.CharField()
    folder = serializers.CharField()
    size = serializers.CharField()
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    topics = serializers.ListField(write_only=True, child=serializers.IntegerField(min_value=0))
    
    def create(self, validated_data):
        print("Data: ", validated_data)
        
        data = Document.objects.create(name = validated_data["name"], 
                                     type=validated_data["type"], 
                                     folder=validated_data["folder"],
                                     size=validated_data["size"]
                                     )
        
        data.topics.set(validated_data["topics"])
        
        return data

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.folder = validated_data.get('folder', instance.folder)
        instance.size = validated_data.get('size', instance.size)
        instance.save()
        return instance