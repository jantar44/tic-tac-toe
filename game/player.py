from random import randint

class Player:

    def __init__(self, player_id, sign):
        self.points = 0
        self.sign = sign
        self.player_id = player_id

    def __str__(self):
        return f'Player {self.player_id}'

    def make_choice(self):
        # first random pick
        return randint(0,2), randint(0,2)

    def make_move(self):
        return self.sign

    def player_won(self):
        print('Player {self} won')


