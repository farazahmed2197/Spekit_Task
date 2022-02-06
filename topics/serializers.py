from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    short_description = serializers.CharField()
    long_description = serializers.CharField()
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    
    def create(self, validated_data):
        print("Data: ", validated_data)
        
        data = Topic.objects.create(**validated_data)
        
        return data

    def update(self, instance, validated_data):
        
        instance.name = validated_data.get('name', instance.name)
        instance.short_description = validated_data.get('short_description', instance.short_description)
        instance.long_description = validated_data.get('long_description', instance.long_description)
        instance.save()
        return instance