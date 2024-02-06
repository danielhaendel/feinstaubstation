from django.core.management.base import BaseCommand
from main.models import *
import csv


class Command(BaseCommand):
    help = 'Importiert Daten aus einer CSV-Datei in die Datenbank'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='Der Pfad zur CSV-Datei')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Person.objects.create(
                    name=row['Name'],
                    alter=row['Alter'],
                    stadt=row['Stadt']
                )

        self.stdout.write(self.style.SUCCESS('Daten erfolgreich importiert.'))
