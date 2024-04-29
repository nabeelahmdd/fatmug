from rest_framework import mixins, viewsets
from myapp.models import (
    Vendor, 
)
from myapp.serializer import (
    VendorSerializer, 
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