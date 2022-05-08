"""Index views."""

from aiohttp.web import RouteTableDef, HTTPFound

from speny.config import settings


routes = RouteTableDef()


@routes.get('/')
async def index_view(request):
    """Index view."""
    raise HTTPFound(f'{settings.TELEGRAM_URL}/{settings.BOT_USERNAME}')
