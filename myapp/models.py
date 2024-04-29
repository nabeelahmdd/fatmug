from django.db import models
import random
import string

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