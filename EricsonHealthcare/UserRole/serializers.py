from rest_framework import serializers
from .models import HOD, Coordinator, InvestigatingOfficer, MedicalOfficer, DataEntryPersonnel


class HODSerializer(serializers.ModelSerializer):
    class Meta:
        model = HOD
        fields = '__all__'