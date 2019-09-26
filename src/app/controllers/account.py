from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from src.app.service.account import AccountService
from src.app.serializer.account import ListSerializer, CreateSerializer
from src.app.controllers.base import BaseController
from src.app.config.exceptions import ServiceUnavailable

class AccountController(BaseController):
    service = AccountService()
    # permission_classes = [IsAuthenticated]
    method_serializer_classes = {
        ('create'): CreateSerializer
    }

    def list(self, request):
        accountList = self.service.getAll()
        paginate_queryset = self.paginate_queryset(accountList)
        serializer = ListSerializer(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def accountDetail(self, request, pk):
        account = self.service.getById(pk=pk)
        serializer = ListSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        account = self.service.getById(pk=pk)
        serializer = CreateSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            account = self.service.getById(pk=pk)
            account.delete()
            content = { 'status': 'NO CONTENT' }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({ 'error': 'SERVER ERROR' }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def specialEndpoint(self, request):
        account = self.service.getSpecificAccount()
        return Response(account, status=status.HTTP_200_OK)

    def exampleRaiseException(self, request):
        raise ServiceUnavailable()