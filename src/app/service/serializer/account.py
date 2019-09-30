from rest_framework import serializers
from src.app.persistence.models.account import AccountModel


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        exclude = ['created_at']


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['name', 'email', 'created_at']


class AccountDTO(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    name = serializers.CharField(max_length=120)
    email = serializers.EmailField()
    created_at = serializers.DateField()