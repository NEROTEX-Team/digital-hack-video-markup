import logging

from aiomisc import Service, entrypoint
from aiomisc_log import basic_config

from video_markup.presentors.rest.config import RestConfig
from video_markup.presentors.rest.service import RestService

log = logging.getLogger("uvicorn")


def main() -> None:
    config = RestConfig()

    basic_config(level=config.log.level, log_format=config.log.format)

    services: list[Service] = [
        RestService(
            host=config.http.host,
            port=config.http.port,
            config=config,
        ),
    ]

    with entrypoint(
        *services,
        log_level=config.log.level,
        log_format=config.log.format,
        pool_size=config.app.pool_size,
        debug=config.app.debug,
    ) as loop:
        log.info(
            "REST service started on address %s:%s",
            config.http.host,
            config.http.port,
        )
        loop.run_forever()


if __name__ == "__main__":
    main()
