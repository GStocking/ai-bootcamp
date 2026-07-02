from fastapi import APIRouter

from models.schemas import CleanRequest, CleanResponse
from services.cleaner import clean_rows

# APIRouter 用来集中管理一组接口。
router = APIRouter()


@router.post("/clean", response_model=CleanResponse)
async def clean(request: CleanRequest):
    # request 是经过 Pydantic 校验后的请求数据。
    # 真正的清洗逻辑放在 services/cleaner.py，接口层只负责接收和返回。
    result = clean_rows(request.rows)
    return result
