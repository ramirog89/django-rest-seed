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

  def dispatch(self, request, *args, **kwargs):
      '''
        Override dispatch method from rest_framework/views.py
        to extend features not tied to to the httpMethod:action
      '''
      self.args = args
      self.kwargs = kwargs
      request = self.initialize_request(request, *args, **kwargs)
      self.request = request
      self.headers = self.default_response_headers

      currentController = type(self)
      # Obtengo los metodos del currentController
      method_list = [func for func in dir(currentController) if callable(getattr(currentController, func)) and "_" not in func]
      
      methodHttp = None
      actionHandler = None

      # capturo el method y action que se paso en el controller.as_view({ 'methodHttp' : 'actionHandler' })
      # @TODO: No es muy python esto.
      for method, action in self.action_map.items():
        actionHandler = action
        methodHttp = method

      try:
          self.initial(request, *args, **kwargs)
          # Armo mi propio check corroborando que el action Handler esta registrado en el Controller
          # y que el metodo que se definio, es el que se uso en la Request
          if actionHandler in method_list and methodHttp == request.method.lower():
              handler = getattr(self, actionHandler, self.http_method_not_allowed)
          else:
              handler = self.http_method_not_allowed
          response = handler(request, *args, **kwargs)
      except Exception as exc:
          response = self.handle_exception(exc)
      self.response = self.finalize_response(request, response, *args, **kwargs)
      return self.response
