import argparse
import csv
from pathlib import Path

from reader import read_csv
from cleaner import clean_data, remove_duplicates
from logger import logger
from writer import write_json


def main():
    parser = argparse.ArgumentParser(description="CSV cleaner CLI")
    parser.add_argument(
        '--input',
        required=True,
        help='数据源路径'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='输出源路径'
    )

    args = parser.parse_args()

    basic_path = Path(__file__).parent
    file_path = basic_path / args.input
    out_path = basic_path / args.output

    try:
        # 1. CSV读取
        origin_data = read_csv(file_path)

        # 2. 错误处理：空数据
        if len(origin_data) == 0:
            logger.error("空数据")
            return 1

        # 3. 数据清洗 + 去重
        cleaned_data = clean_data(origin_data)
        final_data = remove_duplicates(cleaned_data)

        # 4. 输出JSON
        write_json(final_data, out_path)
        logger.info("处理完成")
        return 0
    except FileNotFoundError:
        logger.error("读取失败：文件不存在")
        return 1
    except csv.Error:
        logger.error("读取失败：CSV格式错误")
        return 1
    except Exception as exc:
        logger.error("处理失败：%s", exc)
        return 1


if __name__ == '__main__':
    main()
