from aiohttp import web

from transports import setup_routes


async def init() -> web.Application:
    app = web.Application()
    setup_routes(app)

    return app

if __name__ == '__main__':
    web.run_app(init(), port=8088)