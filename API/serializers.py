from rest_framework import serializers
#from .models import Severity

class severitySerializers(serializers.Serializer):
    distance = serializers.FloatField()
    start_longitude = serializers.FloatField()
    start_latitude = serializers.FloatField()
    crossing_false = serializers.FloatField()
    crossing_true = serializers.FloatField()
    Traffic_Calming_false = serializers.FloatField()
    Traffic_Calming_true = serializers.FloatField()
    humidity = serializers.FloatField()
    precipitation = serializers.FloatField()
    give_way_false = serializers.FloatField()
    give_way_true = serializers.FloatField()
    stop_true = serializers.FloatField()
    stop_false = serializers.FloatField()
    amenity_false = serializers.FloatField()
    amenity_true = serializers.FloatField()
    bump_false = serializers.FloatField()
    bump_true = serializers.FloatField()
    
        