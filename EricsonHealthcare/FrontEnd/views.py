from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError
from django.shortcuts import get_object_or_404, render, redirect


class LoginViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'login.html')

class DashboardViewSet(viewsets.ViewSet):
    def list(self, request):
        return render(request, 'dashboard.html')
