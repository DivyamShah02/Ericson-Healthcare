from rest_framework import serializers
from .models import  UserDetail


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        # fields = ["id", "is_superuser", "username", "first_name", "last_name", "email", "is_staff", "is_active", "date_joined", "role", "user_id", "name", "contact_number", "city", "state"]
        fields = '__all__'
