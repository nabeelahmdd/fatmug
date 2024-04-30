from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myapp.views import (
    VendorView, PurchaseOrderView, VendorPerformanceAPIView,
    PurchaseOrderAcknowledgeAPIView,
)
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()

router.register('vendors', VendorView,
                basename='vendors')
router.register('purchase_orders', PurchaseOrderView,
                basename='purchase_orders')

urlpatterns = [
    path('', include(router.urls)),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('purchase_orders/<int:po_id>/acknowledge/', PurchaseOrderAcknowledgeAPIView.as_view(), name='purchase-order-acknowledge'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]