from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class CompanyRequest(BaseModel):
    company_name: str = Field(..., description="기업명 (예: 삼성전자)")
    ticker: str = Field(..., description="종목코드 (예: 005930)")

# --- DART 분석 요청 ---
class DartAnalysisRequest(BaseModel):
    corp_code: str = Field(..., description="DART 고유 번호", examples=["005930"])
    year: int = Field(..., description="사업연도", examples=[2024])
    report_code: str = Field("11011", description="보고서 코드 (11011: 사업보고서)")

class MarketNewsRequest(BaseModel):
    url: Optional[str] = Field(None, description="분석할 뉴스 URL (있으면 크롤링)")
    content: Optional[str] = Field(None, description="직접 입력한 뉴스 본문 (URL 없으면 사용)")

class MarketSectorRequest(BaseModel):
    sector_name: str = Field(..., description="분석할 섹터명 (예: 반도체, 2차전지)")

# --- RAG 질문 요청 ---
class ChatRequest(BaseModel):
    query: str = Field(..., description="사용자 질문")
    history: List[Dict[str, str]] = Field(List, description="이전 대화 문맥")

class ReportMetadata(BaseModel):
    report_type: str = Field("annual", description="보고서 유형 (annual, quarterly)")
    include_raw_text: bool = Field(False, description="원본 텍스트 포함 여부")

#관리자/ 트리거용
class DataSyncRequest(BaseModel):
    ticker: str = Field(..., description="데이터를 갱신할 종목 코드")