from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CaseViewSet, CaseDetailsViewSet, AddDocumentViewSet, GetAllCaseViewSet, SetInvestigationStatus

router = DefaultRouter()

router.register(r'case-api', CaseViewSet, basename='case-api')
router.register(r'case-details-api', CaseDetailsViewSet, basename='case-details-api')
router.register(r'add-case-document-api', AddDocumentViewSet, basename='add-case-document-api')
router.register(r'get-all-case-api', GetAllCaseViewSet, basename='get-all-case-api')

router.register(r'set-investigation-status-api', SetInvestigationStatus, basename='set-investigation-status-api')

urlpatterns = [
    path('', include(router.urls)),
]
