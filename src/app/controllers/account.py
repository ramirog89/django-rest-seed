from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from src.app.service.account import AccountService
from src.app.serializer.account import ListSerializer, CreateSerializer
from .method_serializer import MethodSerializerView

# class AccountController(ViewSet):
class AccountController(MethodSerializerView, ViewSet):
    service = AccountService()
    # permission_classes = [IsAuthenticated]
    method_serializer_classes = { # hacer funcionar esto con request.action no request.method :)
        ('POST'): CreateSerializer
    }

    def list(self, request):
        accountList = self.service.getAll()
        serializer = ListSerializer(data=accountList)
        serializer.is_valid()
        return JsonResponse(serializer.validated_data)

    def create(self, request):
        print(request)
        return JsonResponse({ 'result': 'something' })

    def update(self, request):
        print(request)
        return JsonResponse({ 'result': 'something' })

    def delete(self, request):
        print(request)
        return JsonResponse({ 'result': 'something' })

    def someBusinessLogicEndpoint(self, request):
        print(request)
        return self.service.getSpecificAccount()
