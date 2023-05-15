from django.db import models


class RawData(models.Model):
    Start_Lng = models.FloatField()
    Start_Lat = models.FloatField()
    Humidity = models.FloatField()
    Distance = models.FloatField()
    Precipitation = models.FloatField()
    Stop = models.BooleanField()
    Give_Way = models.BooleanField()
    Amenity = models.BooleanField()
    Traffic_Calming = models.BooleanField()
    Crossing = models.BooleanField()
    Bump = models.BooleanField()
