from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.

admin.site.site_header = "Administrator Panel"
admin.site.site_title = "Archive"
admin.site.index_title = "Dashboard"

class SuratKeterangan(admin.ModelAdmin):
    list_display = ("file", "upload_time")

    readonly_fields = ["upload_time"]

admin.site.unregister(Group)
admin.site.register(tbl_certificate, SuratKeterangan)