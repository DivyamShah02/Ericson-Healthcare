from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'final-report-api', AddFinalReportViewSet, basename='final-report-api')
router.register(r'render-final-report-api', RenderFinalReportViewSet, basename='render-final-report-api')

urlpatterns = [
    path('', include(router.urls)),
]
