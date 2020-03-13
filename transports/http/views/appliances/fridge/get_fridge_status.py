from typing import Any
from typing import Dict
from typing import List
import random

import aiohttp
from aiohttp import web


async def get_fridge_status(request: aiohttp.web.Request) -> aiohttp.web.Response:
    fridge_results: List[Dict] = []

    for i in range(0, 1000000):
        fridge_status = bool(random.getrandbits(1))
        fridge_lock = bool(random.getrandbits(1))
        fridge_power = random.randint(0, 100)
        fridge_freezer_power = random.randint(0, 100)
        fridge_temperature = random.randint(-20, 0)
        fridge_freezer_temperature = random.randint(-30, -10)

        fridge_data_result: Dict[str, Any] = dict(fridge_status=fridge_status, fridge_power=fridge_power,
                                                  fridge_lock=fridge_lock, fridge_freezer_power=fridge_freezer_power,
                                                  fridge_temperature=fridge_temperature,
                                                  fridge_freezer_temperature=fridge_freezer_temperature)

        fridge_results.append(fridge_data_result)

    return web.json_response(fridge_results)