from logger import logger


def clean_data(data):
    logger.info("开始清洗数据")
    cleaned_data = []

    for row in data:
        item = {
            'name': (row.get('name') or '').strip(),
            'age': int(row.get('age') or 0),
            'city': (row.get('city') or '').strip() or 'Unknown',
            'email': (row.get('email') or '').strip(),
        }
        cleaned_data.append(item)

    logger.info("数据清洗完成")
    return cleaned_data


def remove_duplicates(data):
    logger.info("开始去重")
    seen = set()
    filtered_data = []
    for row in data:
        key = (row['name'], row['age'], row['city'], row['email'])
        if key not in seen:
            seen.add(key)
            filtered_data.append(row)

    logger.info("去重完成")
    return filtered_data
