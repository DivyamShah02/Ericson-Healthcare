from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'create_visit', VisitCreationViewSet, basename='create_visit')
router.register(r'fetch_visits', VisitDetailsViewSet, basename='fetch_visits')

urlpatterns = [
    path('', include(router.urls)),
]