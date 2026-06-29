from pathlib import Path
from reader import read_csv
from cleaner import clean_data, remove_duplicates
from writer import write_json

def main():
    base_dir = Path(__file__).parent
    file_path = base_dir / 'data' / 'staff.csv'
    json_path = base_dir / 'output' / 'output.json'

    origin_data = read_csv(file_path)
    cleaned_data = clean_data(origin_data)
    filtered_data = remove_duplicates(cleaned_data)

    write_json(filtered_data, json_path)

if __name__ == '__main__':
    main()