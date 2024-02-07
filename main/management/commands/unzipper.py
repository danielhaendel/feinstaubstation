import gzip
import shutil
import os


def unzip_all_gz_in_folder(source_folder, target_folder):
    # Stelle sicher, dass der Zielordner existiert
    os.makedirs(target_folder, exist_ok=True)

    # Gehe durch alle Dateien im Quellordner
    for filename in os.listdir(source_folder):
        if filename.endswith(".gz"):
            gz_file_path = os.path.join(source_folder, filename)
            target_file_path = os.path.join(target_folder, filename[:-3])  # Entfernt .gz

            # Entpacke die .gz-Datei
            with gzip.open(gz_file_path, 'rb') as gzipped_file:
                with open(target_file_path, 'wb') as unpacked_file:
                    shutil.copyfileobj(gzipped_file, unpacked_file)

            print(f"File unpacked and saved to: {target_file_path}")


# Absolute Pfade verwenden
#TODO hier muss der Pfad noch angepasst werden und durch eine variable ersetzt werden!
base_dir = 'C:\\Users\\daniel.haendel\\Documents\\dev\\feinstaubstation'
source_folder = os.path.join(base_dir, 'main\\csv_download\\gzFiles')
target_folder = os.path.join(base_dir, 'main\\csv_download')

# Funktion ausführen
unzip_all_gz_in_folder(source_folder, target_folder)



