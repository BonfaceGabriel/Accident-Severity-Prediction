from rest_framework import serializers
from .models import RawData

class RawDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawData
        fields = ['Start_Lng', 'Start_Lat', 'Humidity', 'Distance', 'Precipitation', 'Stop', 'Give_Way', 'Amenity', 'Traffic_Calming', 'Crossing', 'Bump']