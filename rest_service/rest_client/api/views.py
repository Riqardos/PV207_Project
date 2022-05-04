from rest_framework import viewsets
from rest_framework import serializers
from api.models import Vehicle, Incident

# Create your views here.

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class IncidentViewSet(viewsets.ModelViewSet):
    serializer_class = IncidentSerializer
    queryset = Incident.objects.all()
