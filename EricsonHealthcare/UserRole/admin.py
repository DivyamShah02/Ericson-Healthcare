from django.contrib import admin
from .models import UserDetail

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'role', 'name', 'contact_number', 'email')
    search_fields = ('name', 'email', 'contact_number')
    list_filter = ('role',)
