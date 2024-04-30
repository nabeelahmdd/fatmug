from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from myapp.models import (
    Vendor, PurchaseOrder, HistoricalPerformance
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


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = (
        'po_number', 'vendor', 'order_date', 'delivery_date', 'status',
    )
    search_fields = (
        'po_number', 'vendor__name',
    )
    list_filter = (
        'order_date', 'delivery_date',
    )

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)



class HistoricalPerformanceAdmin(admin.ModelAdmin):
    list_display = (
        'vendor', 'date',
    )
    search_fields = (
        'vendor__name',
    )
    list_filter = (
        'date',
    )

admin.site.register(HistoricalPerformance, HistoricalPerformanceAdmin)

