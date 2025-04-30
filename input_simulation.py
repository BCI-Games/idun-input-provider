from asyncio import sleep
from random import random, getrandbits
from server import BroadcastServer


async def start_simulated_input_broadcast_loop(
    server: BroadcastServer, max_delay: float = 2
):
    while True:
        await server.send(str(bool(getrandbits(1))))
        await sleep(random() * max_delay)