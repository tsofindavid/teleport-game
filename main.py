from typing import List

from classes.game_board import GameBoard
from classes.game_cube import GameCube
from classes.info_screen import InfoScreen
from classes.message import GameMessage
from classes.player import Player
from classes.screen import Screen
from utils.input_utils import InputUtils


class Game:
    _screen: Screen = None
    _players: List[Player] = None
    _info_screen: InfoScreen = None
    _game_cube: GameCube = None
    _game_message: GameMessage = None
    _game_board: GameBoard = None

    def __init__(self, game_table_size: int, players: List[Player]):
        self._screen = Screen()
        self._players = players
        self._info_screen = InfoScreen(self._screen, players)
        self._game_cube = GameCube(self._screen, 6, self._info_screen.get_length())
        self._game_message = GameMessage(self._screen, self._game_cube.get_length())
        self._game_board = GameBoard(self._screen, game_table_size, players, self._game_message.get_length())

    def _get_player_by_id(self, id: int) -> Player:
        for player in self._players:
            if player.get_id() == id:
                return player

        raise Exception('Player not found')

    def bootstrap(self):
        self._info_screen.update()
        self._game_cube.ready()
        self._game_board.update()

    def start(self):
        self._info_screen.select_player(self._game_board.get_turn_player().get_id())

        self._game_message.set(f'{self._game_board.get_turn_player().get_name()}, press enter to continue...')
        input('')
        self._game_message.set('')

        self._game_board.make_step(self._game_cube.generate())

        if self._game_board.is_final():
            self._game_message.set(
                f'{self._game_board.get_turn_player().get_name()}, you Win !!!')
            return

        self._game_message.set(f'{self._game_board.get_turn_player().get_name()}, press enter to finalize you turn...')
        input('')

        self._game_board.next_turn_player()
        self._game_board.update()
        self._game_cube.ready()

        return self.start()


if __name__ == "__main__":
    print("This is the Teleport game.")
    print("Welcome and enjoy your time.")
    print("Teleport is a table game and before start you should set the table size.")

    screen_size: int = InputUtils.int_input('Enter the size of game table ( NxN ) ( default: 5 ): ', 5, 10, 5)

    players: List[Player] = []
    for i in range(InputUtils.int_input('Enter the count of players ( example: 1 ): ', 1, 5, 1)):
        name: str = str(InputUtils.str_input(f'Enter the player id={i} name ( default: Player_{i} ): ', f'Player_{i}'))

        players.append(Player(i, name))

    game = Game(screen_size, players)
    game.bootstrap()
    game.start()
