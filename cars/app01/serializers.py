from django.urls import path, include
from .models import Age, Vehicles, Milgr, Location
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class AgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Age
        fields = '__all__'

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('brand', 'model', 'price', 'pr_year', 'km', 'milgr', 'country')

class MilgrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Milgr
        fields = '__all__'

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'