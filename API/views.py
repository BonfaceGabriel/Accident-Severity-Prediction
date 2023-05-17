from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RawDataSerializer
from .mlModel import model
from .forms import SeverityForm
from .preprocessing import preprocess_data
from .models import RawData



@api_view(['GET', 'POST'])
def ml_predict(request):
   if request.method == 'GET':
      form = SeverityForm()
      #serializer = RawDataSerializer(queryset, many=True)
      return render(request, 'predict.html', {'form': form})
   
   if request.method == 'POST':
         form = SeverityForm(request.POST)
         if form.is_valid():
           data = {
                'Start_Lng': form.cleaned_data['Start_Lng'],
                'Start_Lat': form.cleaned_data['Start_Lat'],
                'Humidity(%)': form.cleaned_data['Humidity'],
                'Distance(mi)': form.cleaned_data['Distance'],
                'Precipitation(in)': form.cleaned_data['Precipitation'],
                'Stop': form.cleaned_data['Stop'],
                'Give_Way': form.cleaned_data['Give_Way'],
                'Amenity': form.cleaned_data['Amenity'],
                'Traffic_Calming': form.cleaned_data['Traffic_Calming'],
                'Crossing': form.cleaned_data['Crossing'],
                'Bump': form.cleaned_data['Bump']
            }
           
           preprocessed_data = preprocess_data(data)

           prediction = model.predict(preprocessed_data)
           prediction = prediction[0]

           return render(request, 'result.html', {'prediction': prediction})
         
         else:
            return render(request, 'predict.html', {'form': form})
      
    
@api_view(['GET', 'POST'])
def get_prediction_endpoint(request):
   
   if request.method == 'POST':
         
         user_input = request.data['user_input']
           
         preprocessed_data = preprocess_data(user_input)

         prediction = model.predict(preprocessed_data)
         
         prediction = prediction[0]
         
         return Response({'prediction': prediction})
