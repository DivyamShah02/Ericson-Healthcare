from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError
from django.shortcuts import get_object_or_404, render, redirect


class SorterViewSet(viewsets.ViewSet):
    def create(self, request):
        pass

    def list(self, request):
        pass


from rest_framework import serializers
from .models import ShortlistedProperty

class ShortlistedPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortlistedProperty
        fields = '__all__'
