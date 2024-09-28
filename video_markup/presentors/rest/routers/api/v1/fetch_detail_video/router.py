from fastapi import APIRouter

router = APIRouter(prefix="/videos/{video_id}")


@router.get("")
async def fetch_detail_video() -> None:
    pass
