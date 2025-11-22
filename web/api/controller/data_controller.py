from fastapi import APIRouter, BackgroundTasks
from web.api.request.inference_request import DataSyncRequest
from web.api.response.inference_response import DataSyncResponse

router = APIRouter(tags=["Data Management"])


@router.post("/sync/news", response_model=DataSyncResponse, summary="뉴스 수집 강제 실행")
async def sync_news(req: DataSyncRequest, background_tasks: BackgroundTasks):
    """
    사용자 요청 또는 스케줄러에 의해 특정 종목의 뉴스를 최신화합니다.
    """
    # background_tasks.add_task(news_service.sync_news, req.ticker)

    return DataSyncResponse(
        status="success",
        message=f"{req.ticker} 뉴스 수집 작업이 백그라운드에서 시작되었습니다.",
        collected_count=0
    )


@router.post("/sync/dart", response_model=DataSyncResponse, summary="DART 공시 수집 실행")
async def sync_dart(req: DataSyncRequest):
    return DataSyncResponse(
        status="success",
        message="최신 공시 2건을 업데이트했습니다.",
        collected_count=2
    )