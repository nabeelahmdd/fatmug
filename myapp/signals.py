from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import PurchaseOrder
from myapp.helpers_func import *

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    if instance.status == 'completed':
        update_on_time_delivery_rate(instance.vendor)
        if instance.quality_rating is not None:
            update_quality_rating_avg(instance.vendor)
        update_fulfillment_rate(instance.vendor)

    if instance.acknowledgment_date:
        update_average_response_time(instance.vendor)
    
    record_historical_performance(instance.vendor)