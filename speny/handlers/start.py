"""Start handlers."""

from aiogram import Router
from aiogram.types import Message

from speny.logging import create_logger

logger = create_logger(__name__)


router = Router()


@router.message(commands=['start'])
async def help_handler(message: Message) -> None:
    """Help command handler."""

    await message.reply('Hello, World!')
