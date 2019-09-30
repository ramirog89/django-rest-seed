from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import server_error
from serum import inject

from src.app.service.account import AccountService
from src.app.service.serializer.account import ListSerializer, CreateSerializer
from src.app.controllers.base import BaseController
from src.app.config.exceptions import ServiceUnavailable


class AccountController(BaseController):
    @inject
    def __init__(self, service: AccountService, **kwargs):
        super().__init__(**kwargs)
        self.service = service

    permission_classes = [IsAuthenticated]
    method_serializer_classes = {
        ('create'): CreateSerializer
    }

    def account_detail(self, request, pk):
        account = self.service.get_by_id(pk=pk)
        serializer = ListSerializer(instance=account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request):
        accountList = self.service.get_all()
        paginate_queryset = self.paginate_queryset(accountList)
        serializer = ListSerializer(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = CreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        account = self.service.get_by_id(pk=pk)
        serializer = CreateSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            account = self.service.get_by_id(pk=pk)
            account.delete()
            content = {'status': 'NO CONTENT'}
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        except server_error:
            raise server_error

    def exampleRaiseException(self, request):
        raise ServiceUnavailable()
