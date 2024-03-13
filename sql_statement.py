import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (erstellt sie, wenn nicht vorhanden)
conn = sqlite3.connect('testdatabase.db')

# Cursor erstellen
cursor = conn.cursor()

# SQL-Befehl zum Erstellen einer Tabelle ausführen
cursor.execute('''CREATE TABLE IF NOT EXISTS SDS011 (
                        id SERIAL PRIMARY KEY,
                        sensor_id INTEGER,
                        sensor_type VARCHAR(6),
                        location INTEGER,
                        lat FLOAT,
                        lon FLOAT,
                        timestamp TIMESTAMP,
                        p1 FLOAT,
                        durp1 FLOAT,
                        ratiop1 FLOAT,
                        p2 FLOAT,
                        durp2 FLOAT,
                        ratiop2 FLOAT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS DHT22 (
                    id SERIAL PRIMARY KEY,
                    sensor_id INTEGER,
                    sensor_type VARCHAR(6),
                    location INTEGER,
                    lat FLOAT,
                    lon FLOAT,
                    timestamp TIMESTAMP,
                    temperature FLOAT,
                    humidity FLOAT
                )''')

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()