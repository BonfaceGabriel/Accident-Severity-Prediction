from django import forms

class SeverityForm(forms.Form):
    Start_Lng = forms.FloatField(label='Start Longitude')
    Start_Lat = forms.FloatField(label='Start Latitude')
    Humidity = forms.FloatField(label='Humidity(%)')
    Distance = forms.FloatField(label='Distance(mi)')
    Precipitation = forms.FloatField(label='Precipitation(in)')

    Stop = forms.BooleanField(label='Stop', required=False)
    Give_Way = forms.BooleanField(label='Give Way', required=False)
    Amenity = forms.BooleanField(label='Amenity', required=False)
    Traffic_Calming = forms.BooleanField(label='Traffic Calming', required=False)
    Crossing = forms.BooleanField(label='Crossing', required=False)
    Bump = forms.BooleanField(label='Bump', required=False)