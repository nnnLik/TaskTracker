from rest_framework.serializers import ModelSerializer

from .models import UserNotification


class UserNotificationSerializer(ModelSerializer):
    class Meta:
        model = UserNotification
        fields = (
            "id",
            "user",
            "body",
            "priority",
            "created_at",
        )
