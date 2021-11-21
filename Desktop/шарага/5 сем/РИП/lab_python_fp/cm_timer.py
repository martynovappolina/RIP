import time
from contextlib import contextmanager

class TimerError(Exception):
    pass

class cm_timer_1:
    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Таймер уже работает. Используйте .stop() чтобы его остановить")

        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Таймер не работает. Используйте .start() для его запуска")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(elapsed_time)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *exc_info):
        self.stop()

@contextmanager
def cm_timer_2() -> float:
    start = time.perf_counter()
    yield lambda: time.perf_counter() - start
    #Yield это ключевое слово, которое используется примерно как return —
    # отличие в том, что функция вернёт генератор.
    print(time.perf_counter() - start)

with cm_timer_1():
    time.sleep(2)

print('')

with cm_timer_2():
    time.sleep(2)