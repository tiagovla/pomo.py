import datetime
from pomo.core import Pomo
import asyncio


async def main():
    delta = datetime.timedelta(seconds=10)
    pomo = Pomo(delta)
    pomo.start()

    while pomo.is_running():
        await asyncio.sleep(2)
        print(pomo.remaining_time())


if __name__ == "__main__":
    asyncio.run(main())
