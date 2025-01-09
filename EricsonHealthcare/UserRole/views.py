from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import NotFound, ParseError

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout

from .serializers import UserDetailSerializer
from .models import UserDetail

import random
import string

logger = None

class UserCreationViewSet(viewsets.ViewSet):
    def create(self, request):
        # if not request.user.is_staff:
        #     return Response({"detail": "User not authorized"}, status=status.HTTP_400_BAD_REQUEST)

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
            'admin': 'AD',
        }

        email_already_user = UserDetail.objects.filter(email=email).first()
        contact_number_already_user = UserDetail.objects.filter(contact_number=contact_number).first()

        if email_already_user or contact_number_already_user:
            return Response({"detail": "User already registered."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate role and required fields
        if not name or not contact_number or not email or role not in role_codes.keys():
            return Response({"detail": "Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ensure city and state are provided for relevant roles
        if 'investigator' and (not city or not state):
            return Response({"detail": "City and State are required for this role."}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a unique 10-digit user_id with role code
        user_id = self.generate_user_id(role_code=role_codes[role])

        if str(role_codes[role]) == 'AD':
            user = UserDetail.objects.create_superuser(
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
        
        else:
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
        return Response({'success':True, 'data':user_detail_serializer.data}, status=status.HTTP_201_CREATED)
    
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
        user_roles = ['hod', 'coordinator', 'investigator', 'medical_officer', 'data_entry_personnel', 'admin']

        if user_role not in user_roles:
            return Response({
                "success": False,
                "invalid_user_roles": True,
                "data": None,
            }, status=status.HTTP_400_BAD_REQUEST)

        user_data = UserDetail.objects.filter(role=user_role)
        user_serializer = UserDetailSerializer(user_data, many=True)

        user_serializer_data = user_serializer.data
        len_users = len(user_serializer_data)

        data = {
            "len_users": len_users,
            "users": user_serializer_data
        }
    
        return Response({
                "success": True,
                "invalid_user_roles": False,
                "data": data,
            }, status=status.HTTP_200_OK)


class LoginApiViewSet(viewsets.ViewSet):
    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {
                    "success": False,
                    "user_does_not_exist": False,
                    "wrong_password": False,
                    "error": "Email and password are required."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = UserDetail.objects.filter(email=email).first()
            if not user:
                return Response(
                    {
                        "success": False,
                        "user_does_not_exist": True,
                        "wrong_password": False,
                        "error": None
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # Authenticate the user
            authenticated_user = authenticate(request, username=user.user_id, password=password)
            if not authenticated_user:
                return Response(
                    {
                        "success": False,
                        "user_does_not_exist": False,
                        "wrong_password": True,
                        "error": None
                    },
                    status=status.HTTP_401_UNAUTHORIZED
                )

            # Login the user
            login(request, authenticated_user)
            request.session.set_expiry(30 * 24 * 60 * 60)

            return Response(
                {
                    "success": True,
                    "user_does_not_exist": False,
                    "wrong_password": False,
                    "error": None
                },
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    "success": False,
                    "user_does_not_exist": False,
                    "wrong_password": False,
                    "error": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LogoutApiViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            logout(request)
            return redirect('dashboard-list')

        except Exception as e:
            print(e)
            return redirect('dashboard-list')

class DashboardApiViewSet(viewsets.ViewSet):
    def create(self, request):
        try:
            user = request.user

            if not user.is_authenticated:
                return Response(
                        {
                            "success": False,
                            "user_not_logged_in": True,
                            "data":None,
                            "error": None
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            data = {
                'id': user.id,
                'role': user.role,
                'user_id': user.user_id,
                'name': user.name,
                'contact_number': user.contact_number,
                'city': user.city,
                'state': user.state,
            }

            return Response(
                    {
                        "success": True,
                        "user_not_logged_in": False,
                        "data":data,
                        "error": None
                    },
                    status=status.HTTP_200_OK
                )

        except Exception as e:
            logger.error(e, exc_info=True)
            return Response(
                            {
                                "success": False,
                                "user_not_logged_in": True,
                                "data":None,
                                "error": e
                            },
                            status=status.HTTP_400_BAD_REQUEST
                        )
