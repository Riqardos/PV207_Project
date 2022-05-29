from rest_framework import viewsets
from rest_framework import serializers
from api.models import Vehicle, Incident
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import time




# Create your views here.

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = "__all__"

class IncidentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ["description", "vehicle", "user"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    permission_classes = ()

    @action(detail=True, methods=['post'])
    def set_cleanup_state(self, request, pk=None):
        vehicle = Vehicle.objects.get(pk=pk)
        print(vehicle.state)

        if vehicle.state == 'I':
            vehicle.state = 'M'
            vehicle.save()
            res = VehicleSerializer(instance=vehicle)
            return Response(res.data, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Vehicle is not in idle state'},
                            status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['post'])
    def set_inservice_state(self, request, pk=None):
        vehicle = Vehicle.objects.get(pk=pk)
        print(vehicle.state)

        if vehicle.state == 'I':
            vehicle.state = 'S'
            vehicle.save()
            res = VehicleSerializer(instance=vehicle)
            return Response(res.data, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Vehicle is not in idle state'},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def set_idle_state(self, request, pk=None):
        vehicle = Vehicle.objects.get(pk=pk)
        print(vehicle.state)

        vehicle.state = 'I'
        vehicle.save()

        res = VehicleSerializer(instance=vehicle)
        return Response(res.data, status=status.HTTP_200_OK)

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    permission_classes = ()

    serializer_classes = {
        'list': IncidentSerializer,
        'create': IncidentPostSerializer,
    }

    default_serializer_class = IncidentSerializer # Your default serializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

    def create(self, request, *args, **kwargs):
        serializer = IncidentPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        res = IncidentSerializer(instance=instance)
        return Response(res.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['post'])
    def set_in_progress(self, request, pk=None):
        incident = Incident.objects.get(pk=pk)
        incident.state = 'I'
        incident.save()

        res = IncidentSerializer(instance=incident)
        return Response(res.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def set_declined(self, request, pk=None):
        incident = Incident.objects.get(pk=pk)
        incident.state = 'D'
        incident.save()

        res = IncidentSerializer(instance=incident)
        return Response(res.data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def set_resolved(self, request, pk=None):
        incident = Incident.objects.get(pk=pk)
        incident.state = 'R'
        incident.save()

        res = IncidentSerializer(instance=incident)
        return Response(res.data, status=status.HTTP_200_OK)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = ()



    
