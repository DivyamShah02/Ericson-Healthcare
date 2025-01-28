from rest_framework import serializers
from .models import Case, CaseDetails, InsuranceCompany
from UserRole.models import UserDetail

class CaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class CaseDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseDetails
        fields = '__all__'

class InsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceCompany
        fields = '__all__'
