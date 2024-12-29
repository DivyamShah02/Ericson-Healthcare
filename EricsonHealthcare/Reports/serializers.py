from rest_framework import serializers
from .models import *
from UserRole.models import UserDetail

class PADeathReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = PADeathReport
        fields = '__all__'

class TTDReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = TTDReport
        fields = '__all__'

class HealthClaimReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthClaimReport
        fields = '__all__'

class CashlessClaimReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = CashlessClaimReport
        fields = '__all__'

class ClaimReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClaimReport
        fields = '__all__'

class HDCClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = HDCClosureReport
        fields = '__all__'

class ICLMClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = ICLMClosureReport
        fields = '__all__'

class SecureMindCriticalIllnessReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecureMindCriticalIllnessReport
        fields = '__all__'
