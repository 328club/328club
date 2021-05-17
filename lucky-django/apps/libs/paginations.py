from collections import OrderedDict

from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ApiPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('statusCode', 200),
            ('comments', "成功"),
            ('pagination', {
                'total': self.page.paginator.count,
                'page': self.page.number,
                'page_size': self.page.paginator.per_page,
                'next_page': self.get_next_link(),
                'previous_page': self.get_previous_link(),
            }),
            ('data', data),
        ]), status=status.HTTP_200_OK)
