from django.shortcuts import render
from django.db.models import Max, Avg, Min
from .models import DHT22_3660_2022, SDS011_3659_2022
from datetime import datetime

# Create your views here.
def main(request):
    if request.method == 'POST':
        # Daten vom Formular erhalten
        chosen_date = request.POST.get('date')
        sensor_type = request.POST.get('sensorType')

        # Datum umwandeln, um es in Abfragen zu verwenden
        chosen_date_dt = datetime.strptime(chosen_date, '%Y-%m-%d')

        context = {}

        if sensor_type == 'temperatur' or sensor_type == 'humidity':
            # DHT22 Abfragen
            queryset = DHT22_3660_2022.objects.filter(timestamp__date=chosen_date_dt)

            if sensor_type == 'temperatur':
                context.update({
                    'highest_value': queryset.aggregate(Max('temperature'))['temperature__max'],
                    'average_value': queryset.aggregate(Avg('temperature'))['temperature__avg'],
                    'lowest_value': queryset.aggregate(Min('temperature'))['temperature__min'],
                })
            elif sensor_type == 'humidity':
                context.update({
                    'highest_value': queryset.aggregate(Max('humidity'))['humidity__max'],
                    'average_value': queryset.aggregate(Avg('humidity'))['humidity__avg'],
                    'lowest_value': queryset.aggregate(Min('humidity'))['humidity__min'],
                })

        elif sensor_type == 'pm':
            # SDS011 Abfragen
            queryset = SDS011_3659_2022.objects.filter(timestamp__date=chosen_date_dt)
            context.update({
                'highest_p1': queryset.aggregate(Max('p1'))['p1__max'],
                'average_p1': queryset.aggregate(Avg('p1'))['p1__avg'],
                'lowest_p1': queryset.aggregate(Min('p1'))['p1__min'],
                # Ähnlich können Sie p2-Werte hinzufügen
            })

        # Kontext für das Template
        return render(request, 'main/main.html', context)
    else:
        # Standardmäßig, wenn keine POST-Anfrage erfolgt
        return render(request, 'main/main.html')
