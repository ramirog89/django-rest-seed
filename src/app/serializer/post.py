from rest_framework import serializers
from src.app.models.post import PostModel
from src.app.models.tag import TagModel
from .tag import TagSerializer

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = PostModel
        fields = ['id', 'title', 'body', 'date', 'tags']

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ['title', 'body', 'date']
    
    def create(self, validated_data):
        # tags_data = validated_data.pop('tags')
        post = PostModel.objects.create(**validated_data)
        # for tagId in tags_data:
        #     print(tagId)
            # tag = TagModel.objects.get(pk=tagId)
            # post.add(tag)
        return post