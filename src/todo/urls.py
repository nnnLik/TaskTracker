from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    TaskModelView,
    GlobalCategoryView,
    UserCategoryView,
    TaskGlobalCategoryView,
    TaskUserCategoryView,
)


router_report = DefaultRouter()

router_report.register(r"task", TaskModelView, basename="task")
router_report.register(
    r"global-category", GlobalCategoryView, basename="global-category"
)
router_report.register(r"user-category", UserCategoryView, basename="user-category")


urlpatterns = [
    path(
        "task-global-category/",
        TaskGlobalCategoryView.as_view(),
        name="task-global-category",
    ),
    path(
        "task-user-category/", TaskUserCategoryView.as_view(), name="task-user-category"
    ),
    path("", include(router_report.urls)),
]
