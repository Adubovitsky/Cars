from .models import Age, Vehicles, Milgr, Location
from .serializers import AgeSerializer, VehicleSerializer, MilgrSerializer, LocationSerializer
from rest_framework import routers, serializers, viewsets


class AgeViewSet(viewsets.ModelViewSet):
    queryset = Age.objects.all()
    serializer_class = AgeSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer

class MilgrViewSet(viewsets.ModelViewSet):
    queryset = Milgr.objects.all()
    serializer_class = MilgrSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer