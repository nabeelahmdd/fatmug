from rest_framework import mixins, viewsets
from myapp.models import (
    Vendor, PurchaseOrder
)
from myapp.serializer import (
    VendorSerializer, PurchaseOrderSerializer
)

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