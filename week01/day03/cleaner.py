def clean_data(data):
    cleaned_data = []
    for row in data:
        item = {
            'name': row.get('name', ''),
            'age': int(row.get('age') or 0),
            'city': row.get('city') or 'Unknown',
            'email': row.get('email', ''),
        }
        cleaned_data.append(item)
    return cleaned_data


def remove_duplicates(data):
    seen = set()
    filtered_data = []
    for row in data:
        key = (row['name'],row['age'],row['city'],row['email'])
        if key not in seen:
            seen.append(key)
            filtered_data.append(row)

    return filtered_data