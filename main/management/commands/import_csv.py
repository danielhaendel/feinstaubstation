import os
from django.db import connection

def readFiles(folder):
    for file in os.listdir(folder):
        #print("File:" + folder + "/" + file) Bug Check
        readLines(folder + "/" + file)

def readLines(filepfad):
    file = open(filepfad, "r")
    lines = file.readlines()
    for line in lines:
        # TODO put lines SQL
        print(line)
def convertData(line):  # From string to SQL Light String
    splittet = line.split(";")
    return tuple(splittet)


def checkIfExisting(tableName, timestamp, data):
    with connection.cursor as cursor:
        dht = "(id, sensor_id, sensor_type, location, lat, lon, timestamp, temperature, humidity)"
        sds = "(id, sensor_id, sensor_type, location, lat, lon, timestamp, p1, durp1, ratiop1, p2, durp2, ratiop2)"

        if tableName.contains("sds"):
            cursor.execute("IF NOT EXISTING (select 1 FROM " + tableName + " WHERE timestamp = "+ timestamp +") BEGIN "  
                            "INSERT INTO "+tableName+" " + sds + " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) " +  data)
        else:
            cursor.execute("IF NOT EXISTING (select 1 FROM " + tableName + " WHERE timestamp = " + timestamp + ") BEGIN "
                            "INSERT INTO " + tableName + " " + dht + "VALUES(?,?,?,?,?,?,?,?,?) " + data)
