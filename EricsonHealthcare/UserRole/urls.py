from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'user', UserCreationViewSet, basename='user')
router.register(r'list_users_by_role', ListUsersViewSet, basename='list_users_by_role')

urlpatterns = [
    path('', include(router.urls)),
]
