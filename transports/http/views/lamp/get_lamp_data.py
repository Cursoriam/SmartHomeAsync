from typing import Any
from typing import Dict
from typing import List
import random

import aiohttp
from aiohttp import web


async def get_lamp_data(request: aiohttp.web.Request) -> aiohttp.web.Response:
    turn_on: bool = True
    while True:
        lumen: float = random.randint(0, 30)
        light: float = random.randint(0, 100)
        lamp_data_result: Dict[str, Any] = dict(lumen=lumen, light=light, turn_on=turn_on)
        lamp_tmp: List[Dict] = []
        for i in range(0, 1000000):
            lamp_tmp.append(lamp_data_result)
        return web.json_response(lamp_tmp)
