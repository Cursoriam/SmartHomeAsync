from typing import Any
from typing import Dict
from typing import List
import random

import aiohttp
from aiohttp import web


async def get_coffee_status(request: aiohttp.web.Request) -> aiohttp.web.Response:
    coffee_status = bool(random.getrandbits(1))
    coffee_data_result: Dict[str, Any] = dict(coffee_status=coffee_status)
    cofee_results: List[Dict] = []
    for i in range(0, 1000000):
        cofee_results.append(coffee_data_result)
    return web.json_response(cofee_results)
