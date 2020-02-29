from aiohttp import web

from . import views

HTTP_ROUTES = [
    web.get('/lamp', views.lamp.get_lamp_data)
]
