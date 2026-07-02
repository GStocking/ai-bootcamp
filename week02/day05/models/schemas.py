from typing import Any, List

from pydantic import BaseModel


class RawRow(BaseModel):
    # 输入的一行原始数据。Any 表示这里先允许字符串、数字、空值等不同类型。
    name: Any = None
    age: Any = None
    city: Any = None
    email: Any = None


class CleanRequest(BaseModel):
    # 请求体必须是 {"rows": [...]} 这种结构。
    rows: List[RawRow]


class CleanedRow(BaseModel):
    # 清洗完成后，每一行会变成更稳定的类型。
    name: str
    age: int
    city: str
    email: str


class CleanResponse(BaseModel):
    # 接口最终返回的数据结构。
    total: int
    cleaned_count: int
    removed_duplicates: int
    data: List[CleanedRow]

