from django.db import models


# Table Visit
class Visit(models.Model):
    visit_id = models.IntegerField()
    case_id = models.IntegerField()  # Link to Case ID
    coordinator_id = models.CharField(max_length=100)  # Link to Coordinator ID
    investigator_id = models.CharField(max_length=100)  # Link to Investigating Officer ID
    TYPE_OF_VISIT_CHOICES = [
        ('Hospital', 'Hospital'),
        ('Treating_doctor', 'Treating Doctor'),
        ('Lab', 'Lab'),
        ('Chemist', 'Chemist'),
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
    td_registration_number = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    owner_of_the_hospital = models.CharField(max_length=255)
    doctor_registration_number = models.CharField(max_length=100)
    doctor_contact_number = models.CharField(max_length=15)
    doctor_email = models.CharField(max_length=255)
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
    gst_number = models.CharField(max_length=100)
    drug_license_number = models.CharField(max_length=100)
    questions = models.JSONField(null=True, blank=True)
    answers = models.JSONField(null=True, blank=True)
    document_paths = models.JSONField(null=True, blank=True)
    photo_path = models.JSONField(null=True, blank=True)
