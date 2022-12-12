class Board:
    def __init__(self):
        """Creates board
        """
        self._board = [[0 for i in range(3)] for k in range(3)]

    @property
    def board(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self._board

    def board_setter(self, x, y, sign):
        self._board[y][x] = sign

    def is_empty(self, x, y):
        if self._board[y][x] == 0:
            return True

    def winning_condition(self, sign):
        winning = False
        for row in self.board:
            if row.count(sign) == 3:
                winning = True
        for row in list(map(list, zip(*self.board))):
            if row.count(sign) == 3:
                winning = True
        if [r[i] for i, r in enumerate(self.board)].count(sign)  == 3 or\
             [r[i] for i, r in enumerate(self.board[::-1])].count(sign)  == 3:
             winning = True
        return winning


