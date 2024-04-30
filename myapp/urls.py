from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myapp.views import (
    VendorView, PurchaseOrderView, VendorPerformanceAPIView,
)

router = DefaultRouter()

router.register('vendors', VendorView,
                basename='vendors')
router.register('purchase_orders', PurchaseOrderView,
                basename='purchase_orders')

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
]