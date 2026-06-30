import json
from logger import logger


def write_json(data, out_path):
    logger.info("开始输出JSON")

    with open(out_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    logger.info("JSON输出完成")
