from dataclasses import dataclass, field
from os import environ


@dataclass
class AppConfig:
    title: str = field(default_factory=lambda: environ.get("APP_TITLE", "Video Markup"))
    description: str = field(
        default_factory=lambda: environ.get("APP_DESCRIPTION", "Video Markup")
    )
    version: str = field(default_factory=lambda: environ.get("APP_VERSION", "0.0.1"))
    debug: bool = field(
        default_factory=lambda: environ.get("APP_DEBUG", "false").lower() == "true"
    )
    pool_size: int = field(
        default_factory=lambda: int(environ.get("APP_POOL_SIZE", 10))
    )
