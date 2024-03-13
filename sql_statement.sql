CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id INTEGER DEFAULT 3659,
    sensor_type VARCHAR(6) DEFAULT 'SDS011',
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
);

CREATE TABLE DHT22_3660_2022 (
    id SERIAL PRIMARY KEY,
    sensor_id INTEGER DEFAULT 3660,
    sensor_type VARCHAR(6) DEFAULT 'DHT22',
    location INTEGER,
    lat FLOAT,
    lon FLOAT,
    timestamp TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT
);