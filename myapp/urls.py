from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myapp.views import (
    VendorView
)

router = DefaultRouter()

router.register('vendors', VendorView,
                basename='vendors')

urlpatterns = [
    path('', include(router.urls)),
]