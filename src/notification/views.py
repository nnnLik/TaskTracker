from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from src.core.mixins import CachePagePerUserMixin

from .models import UserNotification
from .serializers import UserNotificationSerializer


class UserNotificationModelView(
    CachePagePerUserMixin,
    viewsets.ReadOnlyModelViewSet,
):
    serializer_class = UserNotificationSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    search_fields = ["task"]
    ordering_fields = ["task"]
    ordering = ["task"]

    def get_queryset(self):
        user = self.request.user
        return UserNotification.objects.filter(user=user)
