from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myapp.views import (
    VendorView, PurchaseOrderView
)

router = DefaultRouter()

router.register('vendors', VendorView,
                basename='vendors')
router.register('purchase_orders', PurchaseOrderView,
                basename='purchase_orders')

urlpatterns = [
    path('', include(router.urls)),
]