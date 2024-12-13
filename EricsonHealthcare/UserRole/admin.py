from django.contrib import admin
from .models import UserDetail

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'role', 'name', 'email', 'is_staff', 'id')
    search_fields = ('user_id', 'name', 'email', 'contact_number')
    list_filter = ('role',)
