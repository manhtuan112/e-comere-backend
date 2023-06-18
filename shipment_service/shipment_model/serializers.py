from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = '__all__'

    def validate(self, attrs):
        return super().validate(attrs)


