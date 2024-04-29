from rest_framework import serializers
from myapp.models import (
    Vendor, 
)

class VendorSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Vendor
        fields = '__all__'