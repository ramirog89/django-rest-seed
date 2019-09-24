from django.utils.decorators import classonlymethod

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from src.app.service.account import AccountService
from src.app.serializer.account import ListSerializer, CreateSerializer
from .Base import BaseController

class AccountController(BaseController):
    service_classes = AccountService()
    # permission_classes = [IsAuthenticated]
    method_serializer_classes = {
        ('create'): CreateSerializer
    }
    
    def list(self, request):
        accountList = self.service.getAll()
        serializer = ListSerializer(data=accountList)
        serializer.is_valid()
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def create(self, request):
        print(request)
        return Response({ 'result': 'something' }, status=status.HTTP_200_OK)

    def update(self, request):
        print(request)
        return Response({ 'result': 'something' }, status=status.HTTP_200_OK)

    def delete(self, request):
        print(request)
        return Response({ 'result': 'something' }, status=status.HTTP_200_OK)

    def someBusinessLogicEndpoint(self, request):
        print(request)
        return self.service.getSpecificAccount()
