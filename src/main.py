from aiohttp import web

from sqlite import init_sqlite

from bootstrap import init_subscriptions
from transports import setup_routes


async def init() -> web.Application:
    app = web.Application()
    setup_routes(app)
    init_sqlite()
    init_subscriptions()
    return app

if __name__ == '__main__':
    web.run_app(init(), host='192.168.100.12', port=8088)

