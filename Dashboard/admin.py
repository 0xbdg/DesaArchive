from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.site_header = "Administrator Panel"
admin.site.site_title = "Archive"
admin.site.index_title = "Dashboard"

class CustomAdmin(UserAdmin):
    model = tbl_admin
    list_display = ['username', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',  'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ( 'username')

admin.site.register(tbl_admin, CustomAdmin)