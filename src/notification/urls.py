from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import UserNotificationModelView

router_report = DefaultRouter()


router_report.register(
    r"user-notification", UserNotificationModelView, basename="user-notification"
)

urlpatterns = [
    path("", include(router_report.urls)),
]
