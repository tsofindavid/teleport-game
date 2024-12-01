from random import randint
from time import sleep

from classes.screen import Screen


class GameCube:
    _screen = None
    _mav_value: int = None
    _padding_top: int = None

    def __init__(self, screen: Screen, mav_value: int = 6, padding_top: int = 0) -> None:
        self._screen = screen
        self._mav_value = mav_value
        self._padding_top = padding_top

    def _set_line(self, y: int, line: str):
        self._screen.set_line(y + self._padding_top, line)

    def get_length(self) -> int:
        return 2 + self._padding_top

    def ready(self):
        self._set_line(0, f'Board Cube: 0')
        self._screen.update()

    def generate(self) -> int:
        value = None

        for _ in range(5):
            value = randint(1, self._mav_value)

            self._set_line(0, f'Board Cube ( generating ): {value}')
            self._screen.update()

            sleep(0.25)

        self._set_line(0, f'Board Cube: {value}')
        self._screen.update()

        return value
