from django.shortcuts import render
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'create_visit', VisitCreationViewSet, basename='create_visit')
router.register(r'visit-api', VisitViewSet, basename='visit-api')
router.register(r'visit-details-api', VisitDetailViewSet, basename='visit-details-api')
router.register(r'update-visit-api', UpdateVisitViewSet, basename='update-visit-api')
router.register(r'start-investigation-visit-api', StartInvestigationVisitViewSet, basename='start-investigation-visit-api')
router.register(r'raise-visit-issue-api', RaiseVisitIssueViewSet, basename='raise-visit-issue-api')
router.register(r'remove-visit-issue-api', RemoveVisitIssueViewSet, basename='remove-visit-issue-api')
router.register(r're-investigate-visit-api', ReInvestigateVisitViewSet, basename='re-investigate-visit-api')
router.register(r'remove-re-investigate-visit-api', RemoveReInvestigateVisitViewSet, basename='remove-re-investigate-visit-api')
router.register(r'delete-visit-api', DeleteVisitViewSet, basename='delete-visit-api')

urlpatterns = [
    path('', include(router.urls)),
]