# Day 03: Employee Data Cleaner

一个非常简单的 CSV 清洗并转换成 JSON 的小工具。

程序会完成：

1. 读取 CSV，转换成 Python 对象
2. 清洗数据
   - 空年龄改成 `0`
   - 空城市改成 `Unknown`
3. 去除重复员工数据
4. 输出 JSON 文件

## 文件说明

- `main.py`：主程序
- `reader.py`：读取 CSV，转换成 Python 对象
- `cleaner.py`：清洗数据并去重
- `writer.py`：保存 JSON 文件
- `data/staff.csv`：示例 CSV 文件

## 运行

```bash
python week01/day03/main.py
```

运行后会生成 `week01/day03/output.json`，并在命令行输出：

```text
共有3条数据
已保存 output.json
```
