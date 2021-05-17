import logging

from rest_framework import serializers
from lucky.models import Lottery

logger = logging.getLogger('django')


class EmptySerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class LotterySerializers(serializers.ModelSerializer):
    class Meta:
        model = Lottery
        fields = "__all__"
