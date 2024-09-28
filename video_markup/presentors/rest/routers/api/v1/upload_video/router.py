from fastapi import APIRouter

router = APIRouter(prefix="/videos/upload")


@router.post("")
async def upload_video() -> None:
    pass
