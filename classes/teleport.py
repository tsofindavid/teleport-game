from enum import Enum


class TeleportType(Enum):
    RED = 1
    GREEN = 2


class Teleport:
    _label: str = None
    _start: int = None
    _end: int = None

    def __init__(self, type: TeleportType, label: str, start: int, end: int) -> None:
        if type == TeleportType.RED:
            self._label = '\x1b[0;37;41m' + label + '\x1b[0m'

        if type == TeleportType.GREEN:
            self._label = '\x1b[0;37;42m' + label + '\x1b[0m'

        self._start = start
        self._end = end

    def get_label(self) -> str:
        return self._label

    def get_start(self) -> int:
        return self._start

    def get_end(self) -> int:
        return self._end
