from django.db import models

# Table HOD
class HOD(models.Model):
    user_id = models.CharField(max_length=100)  # Link to User ID
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

# Table Coordinator
class Coordinator(models.Model):
    user_id = models.CharField(max_length=100)  # Link to User ID
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

# Table InvestigatingOfficer
class InvestigatingOfficer(models.Model):
    user_id = models.CharField(max_length=100)  # Link to User ID
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

# Table MedicalOfficer
class MedicalOfficer(models.Model):
    user_id = models.CharField(max_length=100)  # Link to User ID
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

# Table DataEntryPersonnel
class DataEntryPersonnel(models.Model):
    user_id = models.CharField(max_length=100)  # Link to User ID
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
