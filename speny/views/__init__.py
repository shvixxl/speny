"""Views module."""

from aiohttp.web import Application

from . import auth, index


def add_routes(app: Application) -> None:
    """Add all routes to app."""
    app.add_routes(auth.routes)
    app.add_routes(index.routes)
