from rest_framework import serializers
from src.app.models.tag import TagModel

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = ['id', 'name', 'description']
