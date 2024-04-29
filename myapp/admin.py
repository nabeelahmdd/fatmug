from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from myapp.models import (
    Vendor, 
)
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'vendor_code',
    )
    search_fields = (
        'name', 'vendor_code',
    )
    list_filter = ('vendor_code',)

admin.site.register(Vendor, VendorAdmin)