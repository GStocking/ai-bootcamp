# Day 01: Excel to JSON

一个非常简单的 Excel -> JSON 小工具。

## 文件说明

- `main.py`：主程序
- `excel_reader.py`：读取 Excel，转换成 Python 对象
- `json_writer.py`：保存 JSON 文件
- `info.xlsx`：示例 Excel 文件

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行

```bash
python main.py
```

运行后会生成 `output.json`，并在命令行输出：

```text
共有2条数据
已保存 output.json
```
