from dataclasses import dataclass, field
from os import environ

from video_markup.adapters.database.config import DatabaseConfig
from video_markup.application.config import AppConfig
from video_markup.application.logging import LogConfig


@dataclass(frozen=True, slots=True, kw_only=True)
class HttpConfig:
    host: str = field(default_factory=lambda: environ.get("APP_HTTP_HOST", "0.0.0.0"))
    port: int = field(default_factory=lambda: int(environ.get("APP_HTTP_PORT", 8000)))


@dataclass(frozen=True, slots=True, kw_only=True)
class RestConfig:
    app: AppConfig = field(default_factory=lambda: AppConfig())
    http: HttpConfig = field(default_factory=lambda: HttpConfig())
    log: LogConfig = field(default_factory=lambda: LogConfig())
    db: DatabaseConfig = field(default_factory=lambda: DatabaseConfig())
