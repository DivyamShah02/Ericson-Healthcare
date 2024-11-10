from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError
from django.shortcuts import get_object_or_404, render, redirect


from .serializers import HODSerializer
from .models import HOD

import random
import string

# Create your views here.

class UserCreationViewSet(viewsets.ViewSet):
    def create(self, request):
        # Extract data from the request
        name = request.data.get('name')
        contact_number = request.data.get('contact_number')
        email = request.data.get('email')
        
        if not name or not contact_number or not email:
            return Response({"detail": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a unique 10-digit user_id
        user_id = self.generate_user_id()

        # Create the new HOD instance
        hod = HOD.objects.create(
            user_id=user_id,
            name=name,
            contact_number=contact_number,
            email=email
        )
        
        # Serialize the created HOD instance
        serializer = HODSerializer(hod)

        # Return the response with user_id and other details
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        hods = HOD.objects.all()
        serializer = HODSerializer(hods, many=True)
        return Response(serializer.data)

    def generate_user_id(self):
        while True:
            user_id = ''.join(random.choices(string.digits, k=10))
            if not HOD.objects.filter(user_id=user_id).exists():
                return user_id
