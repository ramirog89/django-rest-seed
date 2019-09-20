from rest_framework import serializers
from src.app.models.post import PostModel

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostModel
        fields = ['title', 'body', 'date']
