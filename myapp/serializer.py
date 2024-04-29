from rest_framework import serializers
from myapp.models import (
    Vendor, PurchaseOrder
)

class VendorSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseOrderSerializer(
    serializers.ModelSerializer
):
    vendor = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    def get_vendor(self, obj):
        serializer = VendorSerializer(obj.vendor, many=False)
        return serializer.data