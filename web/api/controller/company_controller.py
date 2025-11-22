from fastapi import APIRouter
from web.api.request.inference_request import CompanyRequest
from web.api.response.inference_response import CompanyBriefingResponse, CompanyHighlightResponse

# 추후 구현할 서비스/에이전트 임포트 (예시)
# from web.services.news_service import NewsService
# from web.agents.market_agent import MarketAgent

router = APIRouter(tags=["Company Agent"])


@router.post("/briefing", response_model=CompanyBriefingResponse, summary="기업 대시보드 브리핑")
async def generate_briefing(req: CompanyRequest):
    """
    1. [Collector] req.ticker로 최신 뉴스/주가 크롤링
    2. [Agent] 호재/악재 분석 및 요약 생성
    """
    # news_data = await news_service.crawl_recent(req.ticker)
    # result = await market_agent.analyze_briefing(news_data)

    # Mock Return
    return CompanyBriefingResponse(
        introduction=f"{req.company_name}은(는) 글로벌 선두 기업입니다.",
        bull_points=["최신 AI 칩셋 수주 성공", "영업이익 컨센서스 상회 예상"],
        bear_points=["원달러 환율 변동성 확대", "경쟁사 신제품 출시 임박"]
    )


@router.post("/highlight", response_model=CompanyHighlightResponse, summary="투자 하이라이트 상세")
async def generate_highlight(req: CompanyRequest):
    return CompanyHighlightResponse(
        highlight_text=f"### {req.company_name} 투자 포인트\n현재 주가는 저평가 구간으로 판단되며...",
        sentiment="BUY"
    )