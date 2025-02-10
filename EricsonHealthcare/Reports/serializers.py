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

class PermanentPartialDisabilityFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = PermanentPartialDisabilityFinalClosureReport
        fields = '__all__'

class PersonalAccidentHDCFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonalAccidentHDCFinalClosureReport
        fields = '__all__'

class LossOfJobFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = LossOfJobFinalClosureReport
        fields = '__all__'

class SecureMindCriticalIllnessFinalReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecureMindCriticalIllnessFinalReport
        fields = '__all__'

class SecureMindCriticalIllnessDeathFinalReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecureMindCriticalIllnessDeathFinalReport
        fields = '__all__'

class SecureMindCriticalIllnessLiveFinalReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecureMindCriticalIllnessLiveFinalReport
        fields = '__all__'

class GroupCashlessClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupCashlessClosureReport
        fields = '__all__'

class GroupReimbursementFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupReimbursementFinalClosureReport
        fields = '__all__'

class PermanentTotalDisabilityFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = PermanentTotalDisabilityFinalClosureReport
        fields = '__all__'

class RetailCashlessFinalReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = RetailCashlessFinalReport
        fields = '__all__'

class RetailReimbursementFinalReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = RetailReimbursementFinalReport
        fields = '__all__'

class SecureMindClaimHospitalDailyCashFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SecureMindClaimHospitalDailyCashFinalClosureReport
        fields = '__all__'

class SpecificVectorBornDiseaceReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpecificVectorBornDiseaceReport
        fields = '__all__'

class TravelFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = TravelFinalClosureReport
        fields = '__all__'

class WorkmanCompensationFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = WorkmanCompensationFinalClosureReport
        fields = '__all__'

class BrokenBonesSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrokenBones
        fields = '__all__'

class HospitalDailyCashFinalClosureReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = HospitalDailyCashFinalClosureReport
        fields = '__all__'

class LicClaimInvestigationReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = LicClaimInvestigationReport
        fields = '__all__'

class NationlInvestigationReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = NationlInvestigationReport
        fields = '__all__'

class NewIndiaInvestigationReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewIndiaInvestigationReport
        fields = '__all__'

class OrientalFormatInvestigationReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrientalFormatInvestigationReport
        fields = '__all__'

class UnitedIndiaInvestigationReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnitedIndiaInvestigationReport
        fields = '__all__'

class OtherInsuranceInvestigationReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtherInsuranceInvestigationReport
        fields = '__all__'
