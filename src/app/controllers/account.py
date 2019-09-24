from django.http import JsonResponse
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated

from src.app.service.account import AccountService

class AccountController(ViewSet):
    permission_classes = [IsAuthenticated]
    service = AccountService()

    def list(self, request):
        accountList = self.service.getAll()
        return JsonResponse(accountList)

    def create(request):
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
