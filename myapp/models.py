from django.db import models
import random
import string
import json

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique=True, blank=True)
    on_time_delivery_rate = models.FloatField(default=0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    def generate_unique_vendor_code(self):
        clean_name = ''.join(e for e in self.name if e.isalnum())
        random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return f"{clean_name}{random_chars}"

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = self.generate_unique_vendor_code()
        super(Vendor, self).save(*args, **kwargs)


class PurchaseOrder(models.Model):
    STATUS_COICES = (
        ('pending', 'Pending'),
        ('completed,', 'Completed'),
        ('canceled', 'Canceled'),
    )

    po_number = models.CharField(max_length=100, unique=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()  # Stores items as JSON
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_COICES, default="pending")
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = f'PO-{self.id}'
        super(PurchaseOrder, self).save(*args, **kwargs)