import urllib.request
from datetime import datetime, timedelta

def download(sensor_list, base_url):
    '�ffnet die URL f�r jeden Sensor in der Liste, liest den Inhalt und gibt ihn in bin�rer Form zur�ck.'
    data_list = []
    for sensor in sensor_list:
        data = urllib.request.urlopen(base_url + sensor).read()
        data_list.append(data)
    return data_list

def save_csv(data, filenames):
    'Speichert Daten in die angegebenen Dateinamen als CSV-Dateien.'
    for data_item, filename in zip(data, filenames):
        with open(filename, 'wb') as gzip_file:
            gzip_file.write(data_item)
        print(f"GZIP-Datei heruntergeladen: {filename}")

startDatum = datetime(2022, 1, 1)
endDatum = datetime(2022, 12, 31)


while startDatum <= endDatum:
    sensor_list = [
    startDatum.strftime("%Y-%m-%d") + "_sds011_sensor_3659.csv.gz",
    startDatum.strftime("%Y-%m-%d") + "_dht22_sensor_3660.csv.gz"
    ]
    "Hier den Pfad anpassen"
    filenames = [
    "C:\\C_DEV\Testdaten_Feinstaubstation\\" + sensor_list[0],
    "C:\\C_DEV\Testdaten_Feinstaubstation\\" + sensor_list[1]
    ]
    base_url = "https://archive.sensor.community/2022/"+ startDatum.strftime("%Y-%m-%d") +"/"
        
    try:
        data_list = download(sensor_list, base_url)
        save_csv(data_list, filenames)
    except Exception as e:
        print('Datensatz:' + startDatum.strftime("%Y-%m-%d") + ' wurde nicht gefunden.')
        
    startDatum += timedelta(1)