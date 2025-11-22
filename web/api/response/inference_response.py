from pydantic import BaseModel, Field
from typing import List, Optional, Dict


# --- 감성 분석 응답 ---
class SentimentResponse(BaseModel):
    score: float = Field(..., description="감성 점수 (-1.0 ~ 1.0)")
    label: str = Field(..., description="긍정/부정/중립")
    summary: str = Field(..., description="한 줄 요약")

class ReportResponse(BaseModel):
    summary: str = Field(..., description="AI가 생성한 핵심 요약")
    insights: List[str] = Field(..., description="주요 투자 인사이트 리스트")
    key_metrics: Dict[str, str] = Field(..., description="추출된 핵심 재무 지표")

    model_config = {
        "json_schema_extra": {
            "example": {
                "summary": "삼성전자의 매출이 전년 대비 10% 상승했습니다...",
                "insights": ["반도체 업황 회복", "모바일 부문 견조"],
                "key_metrics": {"매출액": "70조", "영업이익": "4.3조"}
            }
        }
    }
class DataSyncResponse(BaseModel):
    status: str = Field(..., description="success 또는 fail")
    message: str = Field(..., description="결과 메시지 (예: 뉴스 5건 수집 완료)")
    collected_count: int = Field(0, description="수집/갱신된 데이터 개수")

class CompanyBriefingResponse(BaseModel):
    introduction: str = Field(..., description="기업 한 줄 소개")
    bull_points: List[str] = Field(..., description="호재 (Positive) 요인")
    bear_points: List[str] = Field(..., description="악재 (Negative/Risk) 요인")

class CompanyHighlightResponse(BaseModel):
    highlight_text: str = Field(..., description="투자 하이라이트 (Markdown 줄글)")
    sentiment: str = Field(..., description="종합 의견 (BUY/HOLD/SELL)")