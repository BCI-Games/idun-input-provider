from psutil import pid_exists
from os import getppid
from asyncio import sleep


async def start_parent_process_dependency_loop(check_delay: float = 0.1):
    while True:
        if not pid_exists(getppid()):
            raise InterruptedError
        await sleep(check_delay)