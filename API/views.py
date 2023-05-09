from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import severitySerializers
from .mlModel import model
from .forms import PredictionForm

# Create your views here.
@api_view(['GET', 'POST'])
def ml_predict(request):
   if request.method == 'GET':
      form = PredictionForm()
      return render(request, 'predict.html', {'form': form})
   
   if request.method == 'POST':
      form = PredictionForm(request.POST)
      if form.is_valid():
         serializers = severitySerializers(data = form.cleaned_data)
         if serializers.is_valid():
            input_data = serializers.validated_data
            prediction = model.predict([list(input_data.values())])
            return render(request, 'predict.html', {'form': form, 'prediction': prediction})
         else:
            return render(request, 'predict.html', {'form': form, 'errors': serializers.errors})
      else:
         return render(request, 'predict.html', {'form': form}) 
         
    

   
