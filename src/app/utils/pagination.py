from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, OrderedDict
from rest_framework.response import Response

class CustomPagination(PageNumberPagination, LimitOffsetPagination):
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'list': data
        })