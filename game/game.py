from .board import Board
from .player import Player

class Game:
    counter = 1

    def __init__(self):
        self.game_number = Game.counter
        Game.counter += 1
        self.board = Board()
        self.player_list = [Player(i+1,i+1) for i in range(2)]

    def __str__(self):
        return f'Game n {self.game_number}'

    def _game_start(self):
        print(f'{self} starts')

    def _game_end(self):
        print(f'{self} ends\n')

    def _game_run(self):
        while True:
            for player in self.player_list:
                while True:
                    x, y = player.make_choice()
                    if self.board.is_empty(x,y):
                        break

                sign = player.make_move()
                self.board.board_setter(x,y,sign)

                if self.board.winning_condition(sign) is True:
                    print(f'Player {player} won!')
                    print(self.board.board)
                    return

    def play_game(self):
        self._game_start()
        self._game_run()
        self._game_end()




