from typing import Iterable, List, Tuple

from models.schemas import RawRow


def clean_data(rows: Iterable[RawRow]):
    # 把每一行原始数据整理成统一格式。
    cleaned_data = []

    for row in rows:
        item = {
            "name": row.get('name'),
            "age": row.get('age') or 0,
            "city": row.get('city', 'Unknown'),
            "email": row.get('email'),
        }
        cleaned_data.append(item)

    return cleaned_data


def remove_duplicates(rows: Iterable[dict]) -> Tuple[List[dict], int]:
    # 用 set 记录已经出现过的数据。如果同一行再次出现，就跳过。
    rows = list(rows)
    seen = set()
    filtered_data = []

    for row in rows:
        key = (row["name"], row["age"], row["city"], row["email"])
        if key not in seen:
            seen.add(key)
            filtered_data.append(row)

    removed_count = len(rows) - len(filtered_data)
    return filtered_data, removed_count


def clean_rows(rows: List[RawRow]):
    # 这是给 API 调用的总入口：先检查，再清洗，最后去重。
    if not rows:
        raise ValueError("rows 不能为空")

    cleaned_data = clean_data(rows)
    final_data, removed_count = remove_duplicates(cleaned_data)

    return {
        "total": len(rows),
        "cleaned_count": len(final_data),
        "removed_duplicates": removed_count,
        "data": final_data,
    }
