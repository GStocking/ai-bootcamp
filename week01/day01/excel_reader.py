from openpyxl import load_workbook


def read_excel(file_name):
    workbook = load_workbook(file_name)
    sheet = workbook.active

    rows = list(sheet.values)
    headers = rows[0]

    data = []

    for row in rows[1:]:
        item = {}

        for index in range(len(headers)):
            key = headers[index]
            value = row[index]
            item[key] = value

        data.append(item)

    return data
