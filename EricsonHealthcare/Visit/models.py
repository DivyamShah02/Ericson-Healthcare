from django.db import models

# Table Visit
class Visit(models.Model):
    visit_id = models.IntegerField()
    case_id = models.IntegerField()  # Link to Case ID
    coordinator_id = models.CharField(max_length=100)  # Link to Coordinator ID
    investigator_id = models.CharField(max_length=100)  # Link to Investigating Officer ID

    investigation_started = models.BooleanField(default=False)
    issue_in_investigation = models.BooleanField(default=False)
    issue_of_investigator = models.CharField(max_length=255, null=True, blank=True, default='')
    submitted_by_investigator = models.BooleanField(default=False)

    re_investigation = models.BooleanField(default=False)
    re_investigation_reason = models.CharField(max_length=255, null=True, blank=True, default='')

    visit_completed = models.BooleanField(default=False)
    TYPE_OF_VISIT_CHOICES = [
        ('Hospital', 'Hospital'),
        ('Treating_doctor', 'Treating Doctor'),
        ('Lab', 'Lab'),
        ('Chemist', 'Chemist'),
        ('Insured', 'Insured'),
    ]
    type_of_visit = models.CharField(max_length=50, choices=TYPE_OF_VISIT_CHOICES)
    tat = models.CharField(max_length=100)  # Time to complete visit and submit data
    VISIT_STATUS_CHOICES = [
        ('Investigation', 'Investigation'),
        ('Investigation_confirmation', 'Investigation Confirmation'),
    ]
    visit_status = models.CharField(max_length=50, choices=VISIT_STATUS_CHOICES)

# Table HospitalVisit
class HospitalVisit(models.Model):
    visit_id = models.IntegerField()  # Link to Visit ID
    hospital_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    doa = models.CharField(max_length=255)
    dod = models.CharField(max_length=255)
    claim_value = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100)
    no_of_beds = models.CharField(max_length=255)
    icu = models.CharField(max_length=255)
    ot = models.CharField(max_length=255)
    nursing_staff = models.CharField(max_length=255)
    rmo = models.CharField(max_length=255)
    
    treating_doctor_degree = models.CharField(max_length=100, null=True, blank=True)
    treating_doctor_registration_number = models.CharField(max_length=100, null=True, blank=True)
    treating_doctor_contact_number = models.CharField(max_length=15, null=True, blank=True)
    treating_doctor_email = models.CharField(max_length=255, null=True, blank=True)

    hospital_owner_name = models.CharField(max_length=255)
    hospital_owner_contact_number = models.CharField(max_length=15)
    hospital_owner_registration_number = models.CharField(max_length=100)

    anaesthetic_doctor_name = models.CharField(max_length=255, null=True, blank=True)
    anaesthetic_doctor_registration_number = models.CharField(max_length=255, null=True, blank=True)
    anaesthetic_doctor_contact_details = models.CharField(max_length=255, null=True, blank=True)
    anaesthetic_doctor_email = models.CharField(max_length=255, null=True, blank=True)
    family_physician_doctor_name = models.CharField(max_length=255, null=True, blank=True)
    family_physician_registration_number = models.CharField(max_length=255, null=True, blank=True)
    family_physician_contact_details = models.CharField(max_length=255, null=True, blank=True)
    family_physician_email = models.CharField(max_length=255, null=True, blank=True)

    work_place = models.BooleanField(default=False)
    corporate_visit = models.BooleanField(default=False)

    questions = models.JSONField(null=True, blank=True)
    answers = models.JSONField(null=True, blank=True)
    document_paths = models.JSONField(null=True, blank=True)
    photo_path = models.JSONField(null=True, blank=True)

# Table LabVisit
class LabVisit(models.Model):
    visit_id = models.IntegerField()  # Link to Visit ID
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    address = models.TextField()
    pathologist_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100)
    questions = models.JSONField(null=True, blank=True)
    answers = models.JSONField(null=True, blank=True)
    document_paths = models.JSONField(null=True, blank=True)
    photo_path = models.JSONField(null=True, blank=True)

# Table PharmacyVisit
class PharmacyVisit(models.Model):
    visit_id = models.IntegerField()  # Link to Visit ID
    name_of_chemist = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=100)
    drug_license_number = models.CharField(max_length=100)
    questions = models.JSONField(null=True, blank=True)
    answers = models.JSONField(null=True, blank=True)
    document_paths = models.JSONField(null=True, blank=True)
    photo_path = models.JSONField(null=True, blank=True)

# Table InsuredVisit
class InsuredVisit(models.Model):
    visit_id = models.IntegerField()  # Link to Visit ID
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    questions = models.JSONField(null=True, blank=True)
    answers = models.JSONField(null=True, blank=True)
    document_paths = models.JSONField(null=True, blank=True)
    photo_path = models.JSONField(null=True, blank=True)

class City(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
