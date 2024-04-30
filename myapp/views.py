from rest_framework import mixins, viewsets
from myapp.models import (
    Vendor, PurchaseOrder,
)
from myapp.serializer import (
    VendorSerializer, PurchaseOrderSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.helpers_func import *

# Create your views here.
class VendorView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    Viewset for handling CRUD operations for Vendor model.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    Manages CRUD operations for PurchaseOrder instances using 'po_number' for lookup.
    Supports filtering by vendor name via a 'search' query parameter.
    """
    lookup_field = 'po_number'
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        """
        Returns a queryset of PurchaseOrders, filtered by vendor name if a 'search' query
        parameter is provided.
        """
        qs = PurchaseOrder.objects.all()
        search = self.request.GET.get('search', None)

        if search:
            qs = qs.filter(vendor__name__icontains=search)

        return qs


class VendorPerformanceAPIView(APIView):
    """
    Retrieve performance metrics for a specific vendor.
    """
    
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response(
                {"message": "Vendor not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )


class PurchaseOrderAcknowledgeAPIView(APIView):
    """
    Allows vendors to acknowledge purchase orders.
    """
    
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()
            update_average_response_time(purchase_order.vendor)
            return Response(
                {"message": "Purchase order acknowledged successfully."}
            )
        except PurchaseOrder.DoesNotExist:
            return Response(
                {"message": "Purchase order not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )