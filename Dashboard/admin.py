from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import *

# Register your models here.

admin.site.site_header = "Kiwariku Archive"
admin.site.site_title = "Kiwariku"
admin.site.index_title = "Index"

class SuratKeterangan(admin.ModelAdmin):
    list_display = ("upload_time", "pdf")

    readonly_fields = ["upload_time"]

    def pdf(self, obj):
        if obj.pdf_file:
            print(f"PDF URL: {obj.pdf_file.url}")  # For debugging purposes
            return format_html(
                '<embed src="{}" type="application/pdf" width="600" height="400" />',
                obj.pdf_file.url
            )
        return 'No file'

    pdf.short_description = 'PDF Preview'

class SuratMasuk(admin.ModelAdmin):
    list_display = ("file", "upload_time")

    readonly_fields = ["upload_time"]

class SuratKeluar(admin.ModelAdmin):
    list_display = ("file", "upload_time")

    readonly_fields = ["upload_time"]

class Asset(admin.ModelAdmin):
    list_display = ("file", "upload_time")

    readonly_fields = ["upload_time"]

admin.site.unregister(Group)
admin.site.register(tbl_certificate, SuratKeterangan)
admin.site.register(tbl_income, SuratMasuk)
admin.site.register(tbl_outcome, SuratKeluar)
admin.site.register(tbl_asset, Asset)