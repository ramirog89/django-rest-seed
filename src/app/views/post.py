from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.app.models.post import PostModel
from src.app.serializer.post import PostSerializer

class PostView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

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

