from django.contrib import admin
from .models import *

@admin.register(HOD)
class HODAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'contact_number', 'email')
    search_fields = ('name', 'email', 'contact_number')
    list_filter = ('user_id',)

@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'contact_number', 'email')
    search_fields = ('name', 'email', 'contact_number')
    list_filter = ('user_id',)

@admin.register(InvestigatingOfficer)
class InvestigatingOfficerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'contact_number', 'email', 'city', 'state')
    search_fields = ('name', 'email', 'city', 'state', 'contact_number')
    list_filter = ('state',)

@admin.register(MedicalOfficer)
class MedicalOfficerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'contact_number', 'email')
    search_fields = ('name', 'email', 'contact_number')
    list_filter = ('user_id',)

@admin.register(DataEntryPersonnel)
class DataEntryPersonnelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'contact_number', 'email')
    search_fields = ('name', 'email', 'contact_number')
    list_filter = ('user_id',)
