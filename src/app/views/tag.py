from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from src.app.models import TagModel
from src.app.serializer import TagSerializer

class TagCreateUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    # permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk=None):
        try:
            tag = TagModel.objects.get(pk=pk)
        except TagModel.DoesNotExist:
            content = {
              'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return tag

    # Get
    def get(self, request, pk):
        tag = self.get_queryset(pk=pk)
        serializer = TagSerializer(tag)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update
    def put(self, request, pk):
        tag = self.get_queryset(pk=pk)
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
      tag = self.get_queryset(pk=pk)
      tag.delete()
      content = {
          'status': 'NO CONTENT'
      }
      return Response(content, status=status.HTTP_204_NO_CONTENT)
   

class TagList(ListCreateAPIView):
    serializer_class = TagSerializer
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
       tagList = TagModel.objects.get_queryset().order_by('id')
       return tagList

    # Get list
    def get(self, request):
        tagList = self.get_queryset()
        paginate_queryset = self.paginate_queryset(tagList)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

