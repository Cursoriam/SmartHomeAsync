from typing import Any
from typing import Dict
from typing import List
import random

import aiohttp
from aiohttp import web


async def get_door_status(request: aiohttp.web.Request) -> aiohttp.web.Response:
    door_results: List[Dict] = []

    for i in range(0, 1000000):
        door_status = bool(random.getrandbits(1))
        door_lock = bool(random.getrandbits(1))
        door_data_result: Dict[str, Any] = dict(door_status=door_status, door_lock=door_lock)

        door_results.append(door_data_result)

    return web.json_response(door_results)
