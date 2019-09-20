from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from src.app.models.post import PostModel
from src.app.serializer.post import PostSerializer

class PostViewSet(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        return Response(PostModel.objects.all())

    def get(self, request, pk=None):
        return Response(PostModel.objects.get(id=pk))

    @action(methods=['post'], detail=False)
    def create(self, request, post=None):
        print(post)
        try:
            post = Post.objects.create(title=post.title, body=post.body, date=post.date)
            post.save();
            return Response('Post created successfully', 200)
        except:
            return Response('Error on create post', 500)

    def update(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def delete(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

