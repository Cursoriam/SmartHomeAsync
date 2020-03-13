from typing import Any
from typing import Dict
from typing import List
import random

import aiohttp
from aiohttp import web


async def get_cooking_time(request: aiohttp.web.Request):
    cooking_results: List[Dict] = []
    for i in range(0, 1000000):
        cooking_time = random.randint(10, 100) * random.random()
        cooking_data_result: Dict[str, Any] = dict(cooking_time=cooking_time)
        cooking_results.append(cooking_data_result)
    return web.json_response(cooking_results)
