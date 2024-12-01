from typing import List

from classes.player import Player
from classes.screen import Screen


class InfoScreen:
    _screen: Screen = None
    _players: List[Player] = None
    _selected: int = None

    def __init__(self, screen: Screen, players: List[Player]) -> None:
        self._screen = screen
        self._players = players

    def get_length(self) -> int:
        return 3 + len(self._players)

    def update(self) -> None:
        self._screen.set_line(0, 'Game: Teleport')
        self._screen.set_line(1, 'Players:')

        for i in range(len(self._players)):
            if self._players[i].get_id() == self._selected:
                self._screen.set_line(i + 2, f'* id: {self._players[i].get_icon()} name: {self._players[i].get_name()}')
            else:
                self._screen.set_line(i + 2, f'* id: {self._players[i].get_id()} name: {self._players[i].get_name()}')

        self._screen.update()

    def select_player(self, id: int) -> None:
        self._selected = id
        self.update()
