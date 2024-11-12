from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, CaseDetailsViewSet

router = DefaultRouter()
router.register(r'create_case', CaseViewSet, basename='case')
router.register(r'add_case_details', CaseDetailsViewSet, basename='case_details')

urlpatterns = [
    path('', include(router.urls)),
]
