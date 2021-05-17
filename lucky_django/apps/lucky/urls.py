from django.urls import path, include
from rest_framework.routers import DefaultRouter

from lucky.viewsets import LotteryViewset

# viewset router
router = DefaultRouter()
router.register(r'lottery', LotteryViewset)

urlpatterns = [
    path('', include(router.urls)),
]
