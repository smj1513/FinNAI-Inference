from fastapi import FastAPI
from web.api.controller import report_controller, company_controller, market_controller, data_controller

description = """
## FinNAI Inference API
이 API는 기업 분석 및 RAG 서비스를 위한 AI Agent 기능을 제공합니다.

### 주요 기능
* **DART 분석**: 전자공시시스템 보고서 요약
* **뉴스 분석**: 최신 기업 뉴스 감성 분석
* **RAG**: 벡터 DB 기반 질의응답
"""

tags_metadata = [
    {"name": "Agent", "description": "LLM 기반 분석 에이전트"},
    {"name": "System", "description": "Health Check 및 시스템 모니터링"},
]

app = FastAPI(
    title="FinNAI Inference",
    description=description,
    version="1.0.0",
    #terms_of_service="http://example.com/terms/",
    # contact={
    #     "name": "Backend Team",
    #     "email": "dev@example.com",
    # },
    # license_info={
    #     "name": "Private License",
    # },
    openapi_tags=tags_metadata, # 태그 메타데이터 등록
    docs_url="/api/v1/inference/docs",

    # 2. 문서 데이터(JSON)가 위치할 경로도 맞춰줍니다.
    openapi_url="/api/v1/inference/openapi.json",
   # root_path="/api/v1/inference"
)

app.include_router(report_controller.router, prefix="/report")
app.include_router(company_controller.router, prefix="/company")
app.include_router(market_controller.router, prefix="/market")
app.include_router(data_controller.router, prefix="/data") # 관리용

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web.main:app", host="0.0.0.0", port=8000, reload=True)