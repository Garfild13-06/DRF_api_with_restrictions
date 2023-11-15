from rest_framework.filters import OrderingFilter
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [OrderingFilter]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    ordering_fields = ['status']

    def get_permissions(self):
        """Получение прав для действий."""
        # print(self.action)
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]

        return []
