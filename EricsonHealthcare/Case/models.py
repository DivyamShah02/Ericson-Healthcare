from django.db import models

# Table InsuranceCompany
class InsuranceCompany(models.Model):
    company_name = models.CharField(max_length=255)
    Retail = models.CharField(max_length=255, null=True, blank=True)
    Group = models.CharField(max_length=255, null=True, blank=True)
    PA_Death = models.CharField(max_length=255, null=True, blank=True)
    SMC_CI_Death_Live = models.CharField(max_length=255, null=True, blank=True)
    TTD = models.CharField(max_length=255, null=True, blank=True)
    PPD = models.CharField(max_length=255, null=True, blank=True)
    PA_HDC = models.CharField(max_length=255, null=True, blank=True)
    SMC_HDC = models.CharField(max_length=255, null=True, blank=True)
    LOJ = models.CharField(max_length=255, null=True, blank=True)
    WC = models.CharField(max_length=255, null=True, blank=True)
    PTD = models.CharField(max_length=255, null=True, blank=True)
    Broken_Bones = models.CharField(max_length=255, null=True, blank=True)
    HDC = models.CharField(max_length=255, null=True, blank=True)

# Table Case
class Case(models.Model):
    case_id = models.IntegerField()
    claim_number = models.CharField(max_length=100, default='')
    hod_id = models.CharField(max_length=100)  # Link to HOD ID
    coordinator_id = models.CharField(max_length=100)  # Link to Coordinator ID
    medical_officer_id = models.CharField(max_length=100, null=True, blank=True)  # Link to Medical Officer ID
    data_entry_id = models.CharField(max_length=100, null=True, blank=True)  # Link to Data Entry Personnel ID
    document_paths = models.JSONField()
    CASE_STATUS_CHOICES = [
        ('Creation', 'Creation'),
        ('Creation_confirmation', 'Creation Confirmation'),
        ('Investigation', 'Investigation'),
        ('Investigation_confirmation', 'Investigation Confirmation'),
        ('Medical', 'Medical'),
        ('Medical_confirmation', 'Medical Confirmation'),
        ('Data_entry', 'Data Entry'),
        ('Data_entry_confirmation', 'Data Entry Confirmation'),
        ('Final_report', 'Final Report'),
        ('Final_report_confirmation', 'Final Report Confirmation'),
        ('Complete', 'Complete'),
    ]
    case_status = models.CharField(max_length=50, choices=CASE_STATUS_CHOICES,
                                    default='Creation')


# Table CaseDetails
class CaseDetails(models.Model):
    case_id = models.IntegerField()  # Link to Case ID
    coordinator_id = models.CharField(max_length=100)  # Link to Coordinator ID
    claim_number = models.CharField(max_length=100)
    insurance_company = models.CharField(max_length=255)  # Link to Insurance Company Name
    type_of_case = models.CharField(max_length=255)
    rate = models.CharField(max_length=255)

    doa = models.CharField(max_length=255, null=True, blank=True)
    dod = models.CharField(max_length=255, null=True, blank=True)
    hospital_name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    claim_value = models.CharField(max_length=255, null=True, blank=True)
    diagnosis = models.CharField(max_length=255, null=True, blank=True)
    insured_name = models.CharField(max_length=255, null=True, blank=True)
    insured_number = models.CharField(max_length=25, null=True, blank=True)
    insured_address = models.TextField(null=True, blank=True)

    medical_officer_remarks = models.TextField(null=True, blank=True)
    final_report = models.CharField(max_length=255, null=True, blank=True)
    STATUS_OF_CLAIM_CHOICES = [
        ('Pass', 'Pass'),
        ('Reject', 'Reject'),
    ]
    status_of_claim = models.CharField(max_length=50, choices=STATUS_OF_CLAIM_CHOICES, null=True, blank=True)
    claim_approved_amount = models.CharField(max_length=100, null=True, blank=True)


# Table FinalReport
class FinalReport(models.Model):
    case_id = models.IntegerField()  # Link to Case ID
    insured_name = models.CharField(max_length=255)
    hospital_name = models.CharField(max_length=255)
    # Add more fields as required for final report completion
