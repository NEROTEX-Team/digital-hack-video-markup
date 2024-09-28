from fastapi import APIRouter

router = APIRouter(prefix="/videos/search")


@router.get("")
async def fetch_list_video() -> None:
    pass
