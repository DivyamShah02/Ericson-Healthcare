from .models import Visit, HospitalVisit, LabVisit, PharmacyVisit
from rest_framework import serializers


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class HospitalVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalVisit
        fields = '__all__'


class LabVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabVisit
        fields = '__all__'


class PharmacyVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyVisit
        fields = '__all__'


class VisitDetailsViewSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
