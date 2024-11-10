from django.contrib import admin
from .models import *

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'visit_id', 'case_id', 'coordinator_id', 'investigator_id', 'type_of_visit', 'visit_status')
    search_fields = ('visit_id', 'case_id', 'type_of_visit')
    list_filter = ('type_of_visit', 'visit_status')

@admin.register(HospitalVisit)
class HospitalVisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'visit_id', 'hospital_name', 'state', 'city', 'claim_value', 'diagnosis')
    search_fields = ('hospital_name', 'state', 'city', 'diagnosis')
    list_filter = ('state', 'city')

@admin.register(LabVisit)
class LabVisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'visit_id', 'name', 'city', 'state', 'address')
    search_fields = ('name', 'city', 'state')
    list_filter = ('city', 'state')

@admin.register(PharmacyVisit)
class PharmacyVisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'visit_id', 'name_of_chemist', 'city', 'gst_number')
    search_fields = ('name_of_chemist', 'city', 'gst_number')
    list_filter = ('city',)
