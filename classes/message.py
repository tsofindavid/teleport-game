from classes.screen import Screen


class GameMessage:
    _screen = None
    _padding_top: int = None

    def __init__(self, screen: Screen, padding_top: int = 0) -> None:
        self._screen = screen
        self._padding_top = padding_top

    def get_length(self) -> int:
        return 2 + self._padding_top

    def _set_line(self, y: int, line: str):
        self._screen.set_line(y + self._padding_top, line)

    def default(self):
        self._set_line(0, '')
        self._screen.update()

    def set(self, message) -> None:
        self._set_line(0, message)
        self._screen.update()
