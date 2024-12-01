class Player:
    _id: int = None
    _name: str = None
    _position: int = 0

    def __init__(self, id: int, name: str) -> None:
        self._id = id
        self._name = name

    def get_id(self) -> int:
        return self._id

    def get_icon(self) -> str:
        return '\x1b[0;30;47m' + str(self._id) + '\x1b[0m'

    def get_name(self) -> str:
        return self._name

    def get_position(self) -> int:
        return self._position

    def set_position(self, position: int) -> None:
        self._position = position
