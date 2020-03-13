from typing import Any
from typing import Dict
from typing import List
import random

import aiohttp
from aiohttp import web


async def get_fan_status(request: aiohttp.web.Request) -> aiohttp.web.Response:
    fan_results: List[Dict] = []

    for i in range(0, 1000000):
        fan_status = bool(random.getrandbits(1))
        fan_power = random.randint(0, 100)
        fan_blow_mode = random.randint(1, 3)
        fan_turn_mode = random.randint(1, 3)

        fan_data_result: Dict[str, Any] = dict(fan_status=fan_status, fan_power=fan_power, fan_blow_mode=fan_blow_mode,
                                               fan_turn_mode=fan_turn_mode)

        fan_results.append(fan_data_result)

    return web.json_response(fan_results)
