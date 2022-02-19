"""Handlers module."""

from aiogram import Router

from . import help, start

router = Router()

router.include_router(help.router)
router.include_router(start.router)
