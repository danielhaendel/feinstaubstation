# Generated by Django 5.0.1 on 2024-02-05 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DHT22_3660_2022',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SDS011_3659_2022',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_id', models.IntegerField()),
                ('sensor_type', models.CharField(max_length=6)),
                ('location', models.IntegerField()),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('p1', models.FloatField()),
                ('durp1', models.FloatField()),
                ('ratiop1', models.FloatField()),
                ('p2', models.FloatField()),
                ('durp2', models.FloatField()),
                ('ratiop2', models.FloatField()),
            ],
        ),
    ]