import csv

from logger import logger


def read_csv(file_path):
    logger.info("开始读取CSV")
    rows = []

    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file, strict=True)

        for row in csv_reader:
            if None in row:
                raise csv.Error("CSV格式错误")
            rows.append(row)

    logger.info("CSV读取完成")
    return rows
