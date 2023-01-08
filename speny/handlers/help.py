"""Help handlers."""

from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(commands=['help'])
async def help_handler(message: Message) -> None:
    """Help command handler."""
    await message.answer('Hello, World!')
