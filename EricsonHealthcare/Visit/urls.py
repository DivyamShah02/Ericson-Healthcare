from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'create_visit', VisitCreationViewSet, basename='create_visit')

urlpatterns = [
    path('', include(router.urls)),
]