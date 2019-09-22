from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import IsAuthenticated

from src.app.serializer import TokenSerializer, EmptySerializer

class AuthenticationView(TokenViewBase, viewsets.GenericViewSet):
  blackList = []

  def get_permissions(self):
    if self.action == 'logout':
        # permission_classes = (IsAuthenticated,)
        permission_classes = ()
    else:
        permission_classes = ()
    return [permission() for permission in permission_classes]
  
  def get_serializer_class(self):
    if self.action == 'login':
      return TokenSerializer
    else:
      return EmptySerializer

  def login(self, request, *args, **kwargs):
    tokenResponse = super().post(request, args, kwargs)
    return tokenResponse

  def logout(self, request):
    # print(tokenResponse.data['access'])
    print(request.META['HTTP_AUTHORIZATION'])
    # self.blackList.append(request.META)
    return Response(None)
