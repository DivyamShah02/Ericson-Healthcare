from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'user', UserCreationViewSet, basename='user')
router.register(r'list_users_by_role', ListUsersViewSet, basename='list_users_by_role')
router.register(r'login-api', LoginApiViewSet, basename='login-api')
router.register(r'dashboard-api', DashboardApiViewSet, basename='dashboard-api')

urlpatterns = [
    path('', include(router.urls)),
]
