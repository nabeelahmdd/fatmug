from myapp.models import PurchaseOrder, HistoricalPerformance
from django.db.models import Avg, F
from django.utils import timezone
def update_on_time_delivery_rate(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    on_time_count = completed_pos.filter(delivery_date__lte=F('order_date')).count()
    if completed_pos.count() > 0:
        vendor.on_time_delivery_rate = (on_time_count / completed_pos.count()) * 100
        vendor.save()

def update_quality_rating_avg(vendor):
    ratings = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    avg_rating = ratings.aggregate(Avg('quality_rating'))['quality_rating__avg']
    vendor.quality_rating_avg = avg_rating if avg_rating else 0
    vendor.save()

def update_average_response_time(vendor):
    acknowledgments = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    total_response_time = sum([(po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledgments])
    avg_response_time = total_response_time / len(acknowledgments) if acknowledgments else 0
    vendor.average_response_time = avg_response_time / 3600  # Convert seconds to hours
    vendor.save()

def update_fulfillment_rate(vendor):
    total_pos = PurchaseOrder.objects.filter(vendor=vendor)
    fulfilled_pos = total_pos.filter(status='completed', quality_rating__isnull=False)  # Assuming 'no issues' implies a quality rating is provided
    if total_pos.count() > 0:
        vendor.fulfillment_rate = (fulfilled_pos.count() / total_pos.count()) * 100
        vendor.save()

def record_historical_performance(vendor):
    HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate,
        date=timezone.now()
    )
