from rest_framework import serializers
from src.app.models.account import AccountModel


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        exclude = ['created_at']


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = ['name', 'email', 'created_at']
