from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from api.api import router

# 创建 FastAPI 应用。app 就是 uvicorn 启动时要找的对象。
app = FastAPI(
    title="CSV Cleaner API",
    description="A small FastAPI service that cleans CSV-like rows from JSON input.",
    version="1.0.0",
)

# 把 api/api.py 里面定义的接口注册到 app 上。
app.include_router(router)


@app.get("/")
async def root():
    # 访问 http://127.0.0.1:8000/ 时，会看到这个简单的健康检查结果。
    return {
        "message": "CSV Cleaner API is running",
        "docs": "/docs",
        "clean_endpoint": "POST /clean",
    }


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # 请求 JSON 格式不对，或者字段类型不符合 Pydantic 模型时，会进入这里。
    return JSONResponse(
        status_code=422,
        content={
            "error": "请求参数无效",
            "details": exc.errors(),
        },
    )


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    # 我们自己主动抛出的 ValueError，比如 rows 为空，会进入这里。
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)},
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # 兜底错误处理：避免程序报错时直接把内部错误暴露给用户。
    return JSONResponse(
        status_code=500,
        content={"error": "服务器内部错误"},
    )
