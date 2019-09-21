from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from src.app.models.post import PostModel
from src.app.serializer.post import PostSerializer

class PostCreateUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk=None):
        try:
            post = PostModel.objects.get(pk=pk)
        except PostModel.DoesNotExist:
            content = {
              'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return post

    # Get
    def get(self, request, pk):
        post = self.get_queryset(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update
    def put(self, request, pk):
        post = self.get_queryset(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
      post = self.get_queryset(pk=pk)
      post.delete()
      content = {
          'status': 'NO CONTENT'
      }
      return Response(content, status=status.HTTP_204_NO_CONTENT)
   

class PostList(ListCreateAPIView):
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
       postList = PostModel.objects.all()
       return postList

    # Get list
    def get(self, request):
        postList = self.get_queryset()
        paginate_queryset = self.paginate_queryset(postList)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

