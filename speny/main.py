"""Main module."""

from aiogram import Bot, Dispatcher

from speny.config import settings
from speny.logging import create_logger
from speny.handlers import router

logger = create_logger(__name__)


dp = Dispatcher()

dp.include_router(router)


def main() -> None:
    """Initializes bot and runs events dispatching."""

    logger.info('Initializing bot...')

    bot = Bot(settings.BOT_TOKEN)

    logger.info('Run')

    dp.run_polling(
        bot,
        polling_timeout=settings.POLLING_TIMEOUT,
        backoff_config=settings.BACKOFF_CONFIG,
    )


if __name__ == '__main__':
    main()
