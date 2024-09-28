from collections.abc import Callable, Sequence

from aiomisc.service.uvicorn import UvicornApplication, UvicornService
from dishka import AsyncContainer, make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from video_markup.application.exceptions import (
    DuplicateObjectException,
    EntityNotFoundError,
)
from video_markup.presentors.rest.config import RestConfig
from video_markup.presentors.rest.handlers import (
    duplicate_exception_handler,
    entity_not_found_exception_handler,
)
from video_markup.presentors.rest.routers.api.router import api_router

ExceptionHandlersType = Sequence[tuple[type[Exception], Callable]]


class RestService(UvicornService):
    ROUTERS: Sequence[APIRouter] = (api_router,)
    EXCEPTION_HANDLERS: ExceptionHandlersType = (
        (DuplicateObjectException, duplicate_exception_handler),
        (EntityNotFoundError, entity_not_found_exception_handler),
    )

    __required__ = ("config",)

    config: RestConfig
    _dishka_container: AsyncContainer

    async def create_application(self) -> UvicornApplication:
        app = FastAPI(
            debug=self.config.app.debug,
            title=self.config.app.title,
            description=self.config.app.description,
            version=self.config.app.version,
            openapi_url="/docs/openapi.json",
            docs_url="/docs/swagger",
            redoc_url="/docs/redoc",
        )
        self._add_middlewares(app=app)
        self._add_routes(app=app)
        self._add_exceptions(app=app)
        self._setup_dependencies(app=app)
        return app

    async def stop(self, exception: Exception | None = None) -> None:
        await self._dishka_container.close(exception=exception)

    def _add_middlewares(self, app: FastAPI) -> None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def _add_routes(self, app: FastAPI) -> None:
        for router in self.ROUTERS:
            app.include_router(router)

    def _add_exceptions(self, app: FastAPI) -> None:
        for exception, handler in self.EXCEPTION_HANDLERS:
            app.add_exception_handler(exception, handler)

    def _setup_dependencies(self, app: FastAPI) -> None:
        self._dishka_container = make_async_container()
        setup_dishka(app=app, container=self._dishka_container)
