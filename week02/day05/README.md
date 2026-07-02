# Day 05: CSV Cleaner API

一个把 CSV Cleaner CLI 改造成 HTTP API 的 FastAPI 练习。

## 功能

- 使用 FastAPI 提供 `POST /clean`
- 使用 Pydantic 校验 JSON 输入
- 清洗字段前后的空格
- 空年龄或非法年龄改成 `0`
- 空城市改成 `Unknown`
- 删除重复数据
- 返回结构化 JSON 结果
- 提供基础异常处理
- 支持 Swagger 页面调试

## 目录结构

```text
week02/day05/
├── main.py              FastAPI 应用入口
├── api/api.py           API 路由
├── models/schemas.py    Pydantic 输入和输出模型
├── services/cleaner.py  数据清洗逻辑
├── requirements.txt     项目依赖
└── README.md            使用说明
```

## 初学者阅读顺序

建议按这个顺序看代码：

1. 先看 `README.md`，知道这个 API 要做什么。
2. 再看 `main.py`，理解 FastAPI 应用从哪里启动。
3. 再看 `api/api.py`，找到 `POST /clean` 这个接口。
4. 再看 `models/schemas.py`，理解请求和返回的数据长什么样。
5. 最后看 `services/cleaner.py`，理解具体清洗逻辑。

可以先记住一句话：

```text
main.py 启动应用 -> api/api.py 定义接口 -> models/schemas.py 定义数据格式 -> services/cleaner.py 处理数据
```

## 请求流程

当你在 Swagger 或 curl 里请求 `POST /clean` 时，程序大概会这样走：

```text
收到 JSON 请求
↓
CleanRequest 检查请求格式
↓
clean() 函数接收请求
↓
clean_rows() 清洗 rows
↓
返回 CleanResponse 格式的 JSON
```

## 安装依赖

进入目录：

```bash
cd week02/day05
```

安装依赖：

```bash
python -m pip install -r requirements.txt
```

如果你的电脑没有 `python` 命令，可以使用：

```bash
python3 -m pip install -r requirements.txt
```

## 启动服务

在 `week02/day05` 目录运行：

```bash
uvicorn main:app --reload
```

启动成功后访问：

- API 首页：http://127.0.0.1:8000
- Swagger 页面：http://127.0.0.1:8000/docs

## 测试接口

请求地址：

```text
POST http://127.0.0.1:8000/clean
```

请求体示例：

```json
{
  "rows": [
    {
      "name": " Tom ",
      "age": "20",
      "city": " Suzhou ",
      "email": " tom@test.com "
    },
    {
      "name": "Lucy",
      "age": "",
      "city": "Shanghai",
      "email": "lucy@test.com"
    },
    {
      "name": "Jack",
      "age": "abc",
      "city": "",
      "email": "jack@test.com"
    },
    {
      "name": "Tom",
      "age": 20,
      "city": "Suzhou",
      "email": "tom@test.com"
    }
  ]
}
```

使用 `curl` 测试：

```bash
curl -X POST http://127.0.0.1:8000/clean \
  -H "Content-Type: application/json" \
  -d '{
    "rows": [
      {"name": " Tom ", "age": "20", "city": " Suzhou ", "email": " tom@test.com "},
      {"name": "Lucy", "age": "", "city": "Shanghai", "email": "lucy@test.com"},
      {"name": "Jack", "age": "abc", "city": "", "email": "jack@test.com"},
      {"name": "Tom", "age": 20, "city": "Suzhou", "email": "tom@test.com"}
    ]
  }'
```

返回示例：

```json
{
  "total": 4,
  "cleaned_count": 3,
  "removed_duplicates": 1,
  "data": [
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
      "age": 0,
      "city": "Unknown",
      "email": "jack@test.com"
    }
  ]
}
```

## 异常示例

如果请求体缺少 `rows`，会返回参数校验错误。

如果 `rows` 为空数组，会返回：

```json
{
  "error": "rows 不能为空"
}
```
