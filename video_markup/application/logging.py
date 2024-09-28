from dataclasses import dataclass, field
from os import environ

from aiomisc_log import LogFormat, LogLevel


def parse_log_level() -> LogLevel:
    level = environ.get("APP_LOG_LEVEL", "info").lower()
    return LogLevel[level]


def parse_log_format() -> LogFormat:
    format = environ.get("APP_LOG_FORMAT", "default").lower()
    return LogFormat[format]


@dataclass(frozen=True, kw_only=True, slots=True)
class LogConfig:
    level: LogLevel = field(default_factory=parse_log_level)
    format: LogFormat = field(default_factory=parse_log_format)
