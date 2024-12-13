from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, CaseDetailsViewSet

router = DefaultRouter()
router.register(r'case-api', CaseViewSet, basename='case-api')
router.register(r'case-details', CaseDetailsViewSet, basename='case-details')

urlpatterns = [
    path('', include(router.urls)),
]
