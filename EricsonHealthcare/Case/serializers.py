from rest_framework import serializers
from .models import Case, CaseDetails
from UserRole.models import UserDetail

class CaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class CaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseDetails
        fields = '__all__'
