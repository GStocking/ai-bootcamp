# Day 04: csv-cleaner-cli

一个新手友好的 CSV 清洗命令行小工具。

程序会完成下面这条流程：

```text
CSV读取
↓
数据清洗
↓
去重
↓
输出JSON
```

## 功能

- 支持命令行参数 `--input` 和 `--output`
- 使用 `logging` 记录运行信息，不使用 `print`
- 读取 CSV 文件
- 清洗数据
  - 空年龄改成 `0`
  - 非数字年龄改成 `0`
  - 空城市改成 `Unknown`
  - 去掉字段前后的空格
- 去除重复数据
- 输出 JSON 文件
- 处理常见错误
  - 文件不存在
  - CSV 格式错误
  - 空数据

## 文件说明

```text
week01/day04/
├── main.py          主程序，负责串起完整流程
├── reader.py        读取 CSV
├── cleaner.py       清洗数据和去重
├── writer.py        输出 JSON
├── logger.py        配置 logging
├── data/input.csv   示例输入文件
└── output/result.json 示例输出文件
```

## 运行方式

进入 `week01/day04` 目录：

```bash
cd week01/day04
python main.py --input data/input.csv --output output/result.json
```

如果你的电脑没有 `python` 命令，可以使用：

```bash
python3 main.py --input data/input.csv --output output/result.json
```

也可以在项目根目录运行：

```bash
python week01/day04/main.py --input data/input.csv --output output/result.json
```

## 输入 CSV 示例

```csv
name,age,city,email
Tom,20,Suzhou,tom@test.com
Lucy,,Shanghai,lucy@test.com
Jack,18,,jack@test.com
Tom,20,Suzhou,tom@test.com
Apple,28,Suzhou,apple@test.com
```

## 输出 JSON 示例

```json
[
  {
    "name": "Tom",
    "age": 20,
    "city": "Suzhou",
    "email": "tom@test.com"
  },
  {
    "name": "Lucy",
    "age": 0,
    "city": "Shanghai",
    "email": "lucy@test.com"
  },
  {
    "name": "Jack",
    "age": 18,
    "city": "Unknown",
    "email": "jack@test.com"
  },
  {
    "name": "Apple",
    "age": 28,
    "city": "Suzhou",
    "email": "apple@test.com"
  }
]
```

## 运行日志示例

程序运行时会在终端显示日志：

```text
INFO - 开始读取CSV
INFO - CSV读取完成
INFO - 开始清洗数据
INFO - 数据清洗完成
INFO - 开始去重
INFO - 去重完成
INFO - 开始输出JSON
INFO - JSON输出完成
INFO - 处理完成
```

如果文件不存在，会显示：

```text
ERROR - 读取失败：文件不存在
```

如果 CSV 格式错误，会显示：

```text
ERROR - 读取失败：CSV格式错误
```

如果 CSV 没有数据，会显示：

```text
ERROR - 空数据
```

## 学习重点

这个练习主要用来熟悉：

- `argparse`：接收命令行参数
- `csv.DictReader`：读取 CSV
- `logging`：替代 `print`
- `try...except`：处理错误
- `json.dump`：输出 JSON 文件
