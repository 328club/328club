from rest_framework import viewsets
from rest_framework.decorators import action

from libs.filters import get_custom_filter_class
from libs.utils import api_success, api_fail
from lucky.models import Lottery
from lucky.serializers import EmptySerializer, LotterySerializers
from libs.paginations import ApiPagination
from libs.permissions import CustomPermissions, AnonymousPremission

from libs.lucky_generator import create_lucky, create_dantuo


class LotteryViewset(viewsets.ModelViewSet):
    """
    retrieve:
    list:
        返回中奖号码
    """
    queryset = Lottery.objects.get_queryset().order_by('id')
    serializer_class = LotterySerializers
    pagination_class = ApiPagination
    permission_classes = (CustomPermissions,)
    filter_class = get_custom_filter_class(Lottery)

    @action(methods=['post'], detail=False, filter_backends=(), filter_class=None, pagination_class=None,
            serializer_class=EmptySerializer, permission_classes=(AnonymousPremission,))
    def lucky(self, request):
        """
        返回普通
        """
        data = self.request.data
        seed = data.get('seed')

        try:
            lottery = create_lucky(seed)
            return api_success(lottery)
        except Exception as e:
            return api_fail(-500, str(e))

    @action(methods=['post'], detail=False, filter_backends=(), filter_class=None, pagination_class=None,
            serializer_class=EmptySerializer, permission_classes=(AnonymousPremission,))
    def dantuo(self, request):
        """
        返回单拖
        """
        data = self.request.data
        seed = data.get('seed')

        try:
            lottery = create_dantuo(seed)
            return api_success(lottery)
        except Exception as e:
            return api_fail(-500, str(e))
