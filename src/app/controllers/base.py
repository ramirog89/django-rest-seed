from rest_framework import exceptions
from rest_framework.viewsets import GenericViewSet

class BaseController(GenericViewSet):
  '''
  Utility class for get different serializer class by method.
  For example:
  method_serializer_classes = {
      ('GET', ): MyModelListViewSerializer,
      ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
  }
  '''
  method_list = None
  method_serializer_classes = None

  def get_queryset(query):
      pass

  def get_serializer_class(self):
      assert self.method_serializer_classes is not None, (
          'Expected view %s should contain method_serializer_classes '
          'to get right serializer class.' %
          (self.__class__.__name__, )
      )
      currentController = type(self)
      self.method_list = [func for func in dir(currentController) if callable(getattr(currentController, func)) and "_" not in func]
      for actions, serializer_cls in self.method_serializer_classes.items():
          if actions in self.method_list:
              return serializer_cls

      raise exceptions.MethodNotAllowed(self.request.method)
