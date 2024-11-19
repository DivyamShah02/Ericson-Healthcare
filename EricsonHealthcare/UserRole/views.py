from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError
from django.shortcuts import get_object_or_404, render, redirect

from .serializers import UserDetailSerializer, ListCoordinatorsSerializer
from .models import UserDetail

import random
import string


class UserCreationViewSet(viewsets.ViewSet):
    def create(self, request):
        # Extract data from the request
        name = request.data.get('name')
        password = request.data.get('password')
        contact_number = request.data.get('contact_number')
        email = request.data.get('email')
        city = request.data.get('city')
        state = request.data.get('state')
        role = request.data.get('role')
        
        role_codes = {
            'hod': 'HO',
            'coordinator': 'CO',
            'investigator': 'IO',
            'medical_officer': 'MO',
            'data_entry_personnel': 'DE',
        }

        # Validate role and required fields
        if not name or not contact_number or not email or role not in role_codes.keys():
            return Response({"detail": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ensure city and state are provided for relevant roles
        if 'investigator' and (not city or not state):
            return Response({"detail": "City and State are required for this role."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a unique 10-digit user_id with role code
        user_id = self.generate_user_id(role_code=role_codes[role])

        # Create the new user instance
        user = UserDetail.objects.create_user(
            user_id=user_id,
            username = user_id,
            password = password,
            name=name,
            contact_number=contact_number,
            email=email,
            city=city,
            state=state,
            role=role,
        )
        
        # Serialize the created UserDetail instance
        user_detail_serializer = UserDetailSerializer(user)
        return Response(user_detail_serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        user_id = request.query_params.get('user_id')  # Use query_params for GET requests
        if not user_id:
            return Response({"detail": "Missing user_id."}, status=status.HTTP_400_BAD_REQUEST)

        user_data_obj = get_object_or_404(UserDetail, user_id=user_id)
        user_data = UserDetailSerializer(user_data_obj).data
        return Response(user_data, status=status.HTTP_200_OK)

    def generate_user_id(self, role_code):
        while True:
            user_id = ''.join(random.choices(string.digits, k=10))
            user_id = role_code + user_id
            if not UserDetail.objects.filter(user_id=user_id).exists():
                return user_id

class ListUsersViewSet(viewsets.ViewSet):
    
    def list(self, request):
        user_role = request.query_params.get('user_role')
        user_roles = ['hod', 'coordinator', 'investigator', 'medical_officer', 'data_entry_personnel']

        if user_role not in user_roles:
            return Response({"detail": "Invalid User Role Name"}, status=status.HTTP_400_BAD_REQUEST)

        user_data = UserDetail.objects.filter(role=user_role)
        user_serializer = ListCoordinatorsSerializer(user_data, many=True)
        user_serializer_data = user_serializer.data
        len_users = len(user_serializer_data)

        return Response(
                        {'len_users': len_users,
                        'data': user_serializer.data,
                        }, status=status.HTTP_200_OK
                    )
    