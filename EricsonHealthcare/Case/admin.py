from django.contrib import admin
from .models import *

@admin.register(InsuranceCompany)
class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'RC', 'RR', 'GC', 'PA_Death', 'HDC')
    search_fields = ('company_name',)
    list_filter = ('company_name',)

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'case_id', 'hod_id', 'coordinator_id', 'medical_officer_id', 'data_entry_id', 'case_status')
    search_fields = ('case_id', 'case_status')
    list_filter = ('case_status',)

@admin.register(CaseDetails)
class CaseDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'case_id', 'coordinator_id', 'claim_number', 'insurance_company', 'type_of_case', 'status_of_claim')
    search_fields = ('claim_number', 'insurance_company', 'type_of_case')
    list_filter = ('status_of_claim',)

@admin.register(FinalReport)
class FinalReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'case_id', 'insured_name', 'hospital_name')
    search_fields = ('insured_name', 'hospital_name')
