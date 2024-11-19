from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, CaseDetailsViewSet

router = DefaultRouter()
router.register(r'create_case', CaseViewSet, basename='case')
router.register(r'case-details', CaseDetailsViewSet, basename='case-details')
router.register(r'get_current_user_cases', CaseViewSet, basename='get_current_user_cases')

urlpatterns = [
    path('', include(router.urls)),
]
