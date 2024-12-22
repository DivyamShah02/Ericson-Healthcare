from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet

router = DefaultRouter()
router.register(r'question-api', QuestionViewSet, basename='question-api')

urlpatterns = [
    path('', include(router.urls)),
]
