from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'', DashboardViewSet, basename='home')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'register', UserRegisterViewSet, basename='register')
router.register(r'dashboard', DashboardViewSet, basename='dashboard')
router.register(r'case_overview', CaseOverviewViewSet, basename='case_overview')
router.register(r'reports', ReportViewSet, basename='reports')


urlpatterns = [
    path('', include(router.urls)),
]

