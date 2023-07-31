from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, permissions, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .models import (
    Task,
    GlobalCategory,
    UserCategory,
    TaskGlobalCategory,
    TaskUserCategory,
)
from .serializers import (
    TaskModelSerializer,
    GlobalCategoryModelSerializer,
    UserCategoryModelSerializer,
    TaskGlobalCategoryModelSerializer,
    TaskUserCategoryModelSerializer,
)


class TaskModelView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskModelSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    search_fields = ["title", "priority", "status"]
    ordering_fields = [
        "title",
        "priority",
        "status",
        "created_at",
        "due_date",
    ]
    ordering = ["title", "priority", "status"]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)


class GlobalCategoryView(ModelViewSet):
    queryset = GlobalCategory.objects.all()
    serializer_class = GlobalCategoryModelSerializer
    permission_classes_by_action = {
        "create": [permissions.IsAdminUser()],
        "update": [permissions.IsAdminUser()],
        "destroy": [permissions.IsAdminUser()],
        "list": [permissions.IsAuthenticated()],
        "retrieve": [permissions.IsAuthenticated()],
        "partial_update": [permissions.IsAdminUser()],
    }
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        "name",
    ]
    filter_fields = [
        "name",
    ]

    def get_permissions(self):
        return self.permission_classes_by_action.get(self.action)


class UserCategoryView(ModelViewSet):
    queryset = UserCategory.objects.all()
    serializer_class = UserCategoryModelSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        "name",
    ]
    filter_fields = [
        "name",
    ]

    def get_queryset(self):
        user = self.request.user
        return UserCategory.objects.filter(user=user)


class TaskGlobalCategoryView(generics.ListCreateAPIView):
    queryset = TaskGlobalCategory.objects.all()
    serializer_class = TaskGlobalCategoryModelSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    search_fields = ["task"]
    ordering_fields = ["task"]
    ordering = ["task"]


class TaskUserCategoryView(generics.ListCreateAPIView):
    queryset = TaskUserCategory.objects.all()
    serializer_class = TaskUserCategoryModelSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    search_fields = ["task"]
    ordering_fields = ["task"]
    ordering = ["task"]
