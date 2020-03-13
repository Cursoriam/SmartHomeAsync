import random

import aiohttp
from aiohttp import web


async def turn_off_cook(request: aiohttp.web.Request):
    cook_id = request['data']['cook_id']
    is_turn_on = bool(random.getrandbits(1))
    if not is_turn_on:
        return web.json_response(dict(turn_off=False, reason='Cook already off'))
    return web.json_response(dict(turn_off=True))
