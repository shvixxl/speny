"""Main module."""

import asyncio

from aiohttp import web

from aiogram import Bot, Dispatcher

from speny.config import settings
from speny.logging import logger
from speny.handlers import router
from speny.views import add_routes


app = web.Application()

add_routes(app)


dp = Dispatcher()

dp.include_router(router)


async def start_web() -> None:
    """Starts web server."""

    logger.info('Starting web server...')

    runner = web.AppRunner(app)

    await runner.setup()

    site = web.TCPSite(
        runner,
        port=settings.PORT,
    )

    await site.start()


async def start_bot() -> None:
    """Starts bot."""

    logger.info('Initializing bot...')

    bot = Bot(
        settings.BOT_TOKEN,
        parse_mode='HTML',
    )

    logger.info('Starting pooling...')

    await dp.start_polling(
        bot,
        polling_timeout=settings.POLLING_TIMEOUT,
        backoff_config=settings.BACKOFF_CONFIG,
    )


async def main() -> None:
    """Starts application."""

    await asyncio.gather(
        start_web(),
        start_bot(),
    )


if __name__ == '__main__':
    asyncio.run(main())
