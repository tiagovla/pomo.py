from enum import Enum, auto
import datetime
from typing import Optional
import asyncio


class State(Enum):
    RUNNING = auto()
    PAUSED = auto()
    DONE = auto()


class Pomo:
    def __init__(
        self, time: datetime.timedelta, loop: Optional[asyncio.AbstractEventLoop] = None
    ):
        self.time_now = datetime.datetime.now()
        self.time: datetime.datetime = self.time_now + time
        self.loop = loop or asyncio.get_running_loop()
        self._state: State = State.PAUSED

    def start(self):
        self._state = State.RUNNING
        self.loop.create_task(self._run())

    async def _run(self):
        while self._state != State.DONE:
            self.time_now = datetime.datetime.now()
            await asyncio.sleep(1)
            if self.time_now > self.time:
                self._state = State.DONE

    def stop(self):
        self._state = State.DONE

    def pause(self):
        self._state = State.PAUSED

    def state(self) -> State:
        return self._state

    def is_running(self) -> bool:
        return self._state != State.DONE

    def remaining_time(self) -> datetime.timedelta:
        diff = self.time - datetime.datetime.now()
        zero = datetime.timedelta(seconds=0)
        return diff if diff > zero else zero
