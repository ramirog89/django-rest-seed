from rest_framework import serializers
from src.app.models.tag import TagModel

class EmptySerializer(serializers.Serializer):
    class Meta:
        fields = ()
