from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myapp.views import (
    VendorView, PurchaseOrderView, VendorPerformanceAPIView,
    PurchaseOrderAcknowledgeAPIView,
)

router = DefaultRouter()

router.register('vendors', VendorView,
                basename='vendors')
router.register('purchase_orders', PurchaseOrderView,
                basename='purchase_orders')

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgeAPIView.as_view(), name='purchase-order-acknowledge'),
]