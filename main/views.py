from django.shortcuts import render
from django.db.models import Max, Avg, Min
from .models import DHT22_3660_2022

# Create your views here.
def main(request):
    # Berechnungen für Temperatur
    highest_temperature = DHT22_3660_2022.objects.aggregate(Max('temperature'))
    average_temperature = DHT22_3660_2022.objects.aggregate(Avg('temperature'))
    lowest_temperature = DHT22_3660_2022.objects.aggregate(Min('temperature'))

    # Berechnungen für Luftfeuchtigkeit
    highest_humidity = DHT22_3660_2022.objects.aggregate(Max('humidity'))
    average_humidity = DHT22_3660_2022.objects.aggregate(Avg('humidity'))
    lowest_humidity = DHT22_3660_2022.objects.aggregate(Min('humidity'))

    # Daten an die Vorlage übergeben
    context = {
        'highest_temperature': highest_temperature['temperature__max'],
        'average_temperature': average_temperature['temperature__avg'],
        'lowest_temperature': lowest_temperature['temperature__min'],
        'highest_humidity': highest_humidity['humidity__max'],
        'average_humidity': average_humidity['humidity__avg'],
        'lowest_humidity': lowest_humidity['humidity__min'],
    }
    return render(request, 'main/main.html', context)