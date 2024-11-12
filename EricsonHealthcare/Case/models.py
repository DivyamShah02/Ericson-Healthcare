from django.db import models

# Table InsuranceCompany
class InsuranceCompany(models.Model):
    company_name = models.CharField(max_length=255)
    RC = models.CharField(max_length=255)
    RR = models.CharField(max_length=255)
    GC = models.CharField(max_length=255)
    GR = models.CharField(max_length=255)
    PA_Death = models.CharField(max_length=255)
    IPA = models.CharField(max_length=255)
    GPA = models.CharField(max_length=255)
    SMC_PA = models.CharField(max_length=255)
    HDC = models.CharField(max_length=255)
    LOJ = models.CharField(max_length=255)
    WC = models.CharField(max_length=255)
    PTD = models.CharField(max_length=255)
    TTD = models.CharField(max_length=255)
    SMC = models.CharField(max_length=255)
    PPD = models.CharField(max_length=255)

# Table Case
class Case(models.Model):
    case_id = models.IntegerField()
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
    medical_officer_remarks = models.TextField(null=True, blank=True)
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
