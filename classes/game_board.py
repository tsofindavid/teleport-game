from time import sleep
from typing import List

from classes.player import Player
from classes.screen import Screen
from classes.teleports_generator import TeleportsGenerator
from utils.iterators_utils import IteratorsUtils


class GameBoard:
    _board_x_scale: int = 3
    _board_y_scale: int = 2
    _padding_top: int = None
    _screen: Screen = None
    _table_size: int = None
    _last_point: int = None
    _players: List[Player] = None
    _turn_player: Player = None
    _final: bool = False

    def __init__(self, screen: Screen, tabel_size: int, players: List[Player], padding_top: int = 0) -> None:
        self._screen = screen
        self._table_size = tabel_size
        self._last_point = int(tabel_size ** 2 - 1)
        self._players = players
        self._turn_player = players[0]
        self._padding_top = padding_top
        self._teleports = TeleportsGenerator(int(tabel_size / 2), self._last_point - 1).generate()

    def _set_to_screen(self, x: int, y: int, value: str, padding: int = 1):
        self._screen.set(
            x + (padding * self._board_x_scale),
            y + self._padding_top + (padding * self._board_y_scale),
            value)

    def get_turn_player(self) -> Player:
        return self._turn_player

    def next_turn_player(self):
        i = self._players.index(self._turn_player)

        if i < len(self._players) - 1:
            self._turn_player = self._players[i + 1]
            return

        self._turn_player = self._players[0]

    def is_final(self) -> bool:
        return self._final

    def update(self):
        for y, y_mapped in IteratorsUtils.get_range(self._table_size + 1, self._board_y_scale, 1):
            self._set_to_screen(0, y_mapped, str(y - 1), 0)

        for x, x_mapped in IteratorsUtils.get_range(self._table_size + 1, self._board_x_scale, 1):
            self._set_to_screen(x_mapped, 0, str(x - 1), 0)

        for y, y_mapped in IteratorsUtils.get_range(self._table_size, self._board_y_scale):
            for x, x_mapped in IteratorsUtils.get_range(self._table_size, self._board_x_scale):
                self._set_to_screen(x_mapped, y_mapped, '·')

        self._set_to_screen(0, 0, '+')
        self._set_to_screen(
            (self._table_size - 1) * self._board_x_scale,
            (self._table_size - 1) * self._board_y_scale,
            '*'
        )

        for teleport in self._teleports:
            row_start = (teleport.get_start() // self._table_size)
            column_start = (teleport.get_start() % self._table_size)

            if row_start % 2:
                self._set_to_screen(
                    (self._table_size - 1 - column_start) * self._board_x_scale,
                    row_start * self._board_y_scale,
                    teleport.get_label()
                )
            else:
                self._set_to_screen(
                    column_start * self._board_x_scale,
                    row_start * self._board_y_scale,
                    teleport.get_label()
                )

            row_end = (teleport.get_end() // self._table_size)
            column_end = (teleport.get_end() % self._table_size)

            if row_end % 2:
                self._set_to_screen(
                    (self._table_size - 1 - column_end) * self._board_x_scale,
                    row_end * self._board_y_scale,
                    teleport.get_label()
                )
            else:
                self._set_to_screen(
                    column_end * self._board_x_scale,
                    row_end * self._board_y_scale,
                    teleport.get_label()
                )

        for player in self._players:
            if player.get_id() == self._turn_player.get_id():
                row = (player.get_position() // self._table_size)
                column = (player.get_position() % self._table_size)

                if row % 2:
                    self._set_to_screen(
                        (self._table_size - 1 - column) * self._board_x_scale,
                        row * self._board_y_scale,
                        player.get_icon()
                    )
                else:
                    self._set_to_screen(
                        column * self._board_x_scale,
                        row * self._board_y_scale,
                        player.get_icon()
                    )

        self._screen.update()

    def make_step(self, cube_value: int):
        player = self.get_turn_player()

        position = player.get_position()

        for i in range(cube_value + 1):
            if position + i > self._last_point:
                self.get_turn_player().set_position(self._last_point)
                self._final = True
                break
            else:
                self.get_turn_player().set_position(position + i)

            self.update()
            sleep(1)

        if self._final:
            return

        position = player.get_position()

        for teleport in self._teleports:
            if teleport.get_start() == position:
                player.set_position(teleport.get_end())

        self.update()
