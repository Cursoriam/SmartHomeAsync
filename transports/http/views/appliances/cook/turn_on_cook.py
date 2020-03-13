import random

import aiohttp
from aiohttp import web


async def turn_on_cook(request: aiohttp.web.Request):
    cook_id = request['data']['cook_id']
    is_turn_on = bool(random.getrandbits(1))
    if is_turn_on:
        return web.json_response(dict(turn_on=False, reason='Cook already on'))
    return web.json_response(dict(turn_on=True))
