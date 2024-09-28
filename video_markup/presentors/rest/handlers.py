from http import HTTPStatus

from fastapi import Request
from fastapi.responses import JSONResponse

from video_markup.application.exceptions import (
    DuplicateObjectException,
    EntityNotFoundError,
)


async def duplicate_exception_handler(
    request: Request, exc: DuplicateObjectException
) -> JSONResponse:
    return JSONResponse(
        content={
            "message": exc.message,
        },
        status_code=HTTPStatus.CONFLICT,
    )


async def entity_not_found_exception_handler(
    request: Request, exc: EntityNotFoundError
) -> JSONResponse:
    return JSONResponse(
        content={
            "message": exc.message,
        },
        status_code=HTTPStatus.NOT_FOUND,
    )
