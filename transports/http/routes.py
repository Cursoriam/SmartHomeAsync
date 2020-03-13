from aiohttp import web

from . import views

HTTP_ROUTES = [
    web.get('/light', views.light.get_lamp_data),
    web.get('/coffee_machine/status', views.coffee_machine.get_coffee_status)
]
