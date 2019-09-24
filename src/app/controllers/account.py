from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from src.app.service.account import AccountService

class AccountController(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @require_http_methods(["GET"])
    def list(self, request):
        print(request)
        return HttpResponse({ 'result': 'something' })

    @require_http_methods(["POST"])
    def create(self, request):
        print(request)
        return HttpResponse({ 'result': 'something' })

    @require_http_methods(["PUT"])
    def update(self, request):
        print(request)
        return HttpResponse({ 'result': 'something' })

    @require_http_methods(["DELETE"])
    def delete(self, request):
        print(request)
        return HttpResponse({ 'result': 'something' })

    @require_http_methods(["GET"])
    def someBusinessLogicEndpoint(self, request):
        print(request)
        return AccountService.getSpecificAccount()
