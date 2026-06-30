import json
import os

from logger import logger


def write_json(data, out_path):
    logger.info("开始输出JSON")
    output_dir = os.path.dirname(out_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(out_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

    logger.info("JSON输出完成")
