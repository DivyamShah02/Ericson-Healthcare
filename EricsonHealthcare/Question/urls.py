from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, VisitQuestionViewSet

router = DefaultRouter()
router.register(r'question-api', QuestionViewSet, basename='question-api')
router.register(r'visit-question-api', VisitQuestionViewSet, basename='visit-question-api')

urlpatterns = [
    path('', include(router.urls)),
]
