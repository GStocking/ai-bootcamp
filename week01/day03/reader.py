import csv

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        csv_data = csv.DictReader(file)
        return list(csv_data)