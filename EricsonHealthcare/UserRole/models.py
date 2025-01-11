from django.contrib.auth.models import AbstractUser
from django.db import models

class UserDetail(AbstractUser):
    ROLE_CHOICES = [
        ('hod', 'HOD'),
        ('coordinator', 'Coordinator'),
        ('investigator', 'InvestigatingOfficer'),
        ('medical_officer', 'MedicalOfficer'),
        ('data_entry_personnel', 'DataEntryPersonnel'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    user_id = models.CharField(max_length=12, unique=True)  # Ensure user_id is unique
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    device_id = models.CharField(max_length=255, null=True, blank=True, default='')
