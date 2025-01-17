from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'user', UserCreationViewSet, basename='user')
router.register(r'list_users_by_role', ListUsersViewSet, basename='list_users_by_role')
router.register(r'login-api', LoginApiViewSet, basename='login-api')
router.register(r'logout-api', LogoutApiViewSet, basename='logout-api')
router.register(r'save-device-id-api', SaveDeviceIdApiViewSet, basename='save-device-id-api')
router.register(r'dashboard-api', DashboardApiViewSet, basename='dashboard-api')
router.register(r'get-all-users-api', GetAllUsersApiViewSet, basename='get-all-users-api')
router.register(r'get-report-info-api', GetReportInfoApiViewSet, basename='get-report-info-api')
router.register(r'change-password-api', ChangePasswordApiViewSet, basename='change-password-api')
router.register(r'is-user-authorized-api', IsUserAuthorizedApiViewSet, basename='is-user-authorized-api')

urlpatterns = [
    path('', include(router.urls)),
]
