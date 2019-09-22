from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.app.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def create(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def update(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def delete(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

