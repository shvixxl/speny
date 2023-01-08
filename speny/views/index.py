"""Index views."""

from typing import NoReturn

from aiohttp.web import HTTPFound, RouteTableDef

from speny.config import settings

routes = RouteTableDef()


@routes.get('/')
async def index_view(request) -> NoReturn:
    """Index view."""
    raise HTTPFound(f'{settings.TELEGRAM_URL}/{settings.BOT_USERNAME}')
