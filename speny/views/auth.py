"""Auth views."""

from typing import NoReturn

from aiohttp.web import RouteTableDef, Request, HTTPFound

from speny.config import settings


routes = RouteTableDef()


@routes.get('/auth')
async def auth_view(request: Request) -> NoReturn:
    """Auth view."""
    raise HTTPFound(f'{settings.TELEGRAM_URL}/{settings.BOT_USERNAME}')
