from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'final-report-api', AddFinalReportViewSet, basename='final-report-api')

urlpatterns = [
    path('', include(router.urls)),
]
