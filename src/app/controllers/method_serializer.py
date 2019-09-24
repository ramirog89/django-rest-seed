from rest_framework import exceptions
import inspect

class MethodSerializerView(object):
    '''
    Utility class for get different serializer class by method.
    For example:
    method_serializer_classes = {
        ('GET', ): MyModelListViewSerializer,
        ('PUT', 'PATCH'): MyModelCreateUpdateSerializer
    }
    '''
    method_serializer_classes = None

    def get_serializer_class(self):
        assert self.method_serializer_classes is not None, (
            'Expected view %s should contain method_serializer_classes '
            'to get right serializer class.' %
            (self.__class__.__name__, )
        )
        # m = inspect.getmembers(self.__class__.__name__)
        # method_list = [func for func in dir(self.__class__.__name__) if callable(getattr(__class__.__name__, func))]
        # print("method_list", method_list)
        # print("entra aca entonces", self.__class__.__name__)
        # print(self.request.method)
        print(self.method_serializer_classes.items())
        for actions, serializer_cls in self.method_serializer_classes.items():
            print(serializer_cls)
            if self.request.method in actions:
                return serializer_cls

        raise exceptions.MethodNotAllowed(self.request.method)
