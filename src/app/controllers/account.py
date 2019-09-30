from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from serum import inject

from src.app.service.account import AccountService
from src.app.service.serializer.account import AccountDTO
from src.app.config.exceptions import EntityNotFound


class AccountController(GenericViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = AccountDTO

    @inject
    def __init__(self, service: AccountService, **kwargs):
        super().__init__(**kwargs)
        self.service = service

    def get_queryset(query):
        pass

    def account_detail(self, request, pk):
        try:
            account = self.service.get_by_id(pk=pk)
            return Response(account, status.HTTP_200_OK)
        except Exception:
            raise EntityNotFound

    def list(self, request):
        accountList = self.service.get_all()
        paginate_queryset = self.paginate_queryset(accountList)
        dtos = AccountDTO(paginate_queryset, many=True)
        return self.get_paginated_response(dtos.data)

    def create(self, request):
        dto = AccountDTO(data=request.data)
        if dto.is_valid():
            return Response(self.service.create(dto), status=status.HTTP_201_CREATED)
        return Response(dto.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        dto = AccountDTO(data=request.data)
        if dto.is_valid():
            return Response(self.service.update(dto, pk), status=status.HTTP_200_OK)
        return Response(dto.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            self.service.delete(pk=pk)
            content = {'status': 'NO CONTENT'}
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response({'error': 'SERVER ERROR'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
