from player import Player


class BoardError(Exception):
    """Base class for all board errors
    """

    def __init__(self, message):
        self.message = message


class InvalidPositionError(BoardError):
    """Called when a position requested is out of bounds
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class PositionOccupiedError(BoardError):
    """Called when a position requested is already occupied
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Board:
    """Base class for all Board Functions
    """

    def __init__(self, size=3) -> None:
        self.size = size
        self.grid = self._create_2d_grid()

    def _create_2d_grid(self):  # -> None:
        h, w = self.size, self.size  # define the size of your 2D list
        return [[None for _ in range(w)] for _ in range(h)]

    def is_full(self) -> bool:
        for inner_list in self.grid:
            for item in inner_list:
                if item is None:
                    return False
        return True

    def is_position_occupied(self, row, col) -> bool:
        return self.grid[row][col] is not None

    def is_position_invalid(self, row, col) -> bool:
        if 0 < row > self.size or 0 < col > self.size:
            return True
        return False

    def make_move(self, row, col, player) -> None:
        if self.is_position_invalid(row, col):
            raise InvalidPositionError("Invalid position - Please try again")
            # print("Invalid position")
        if self.is_position_occupied(row, col):
            raise PositionOccupiedError("Position already occupied - Please try again")
            # print("Position already occupied")
        self.grid[row][col] = player.symbol

    def get_winner(self) -> None | Player:
        return self._has_horizontal_winner() or self._has_vertical_winner() or self._has_diagonal_winner()

    def _has_horizontal_winner(self) -> None | Player:
        for row in self.grid:
            if row[0] is not None and row.count(row[0]) == len(row):
                winner = row[0]
                return Player(winner)

    def _has_vertical_winner(self) -> None | Player:
        for columns in range(len(self.grid[0])):
            checklist = []
            for row in self.grid:
                checklist.append(row[columns])
            if checklist[0] is not None and checklist.count(checklist[0]) == len(checklist):
                winner = checklist[0]
                return Player(winner)

    def _has_diagonal_winner(self) -> None | Player:
        forward_diagonal = []
        for idx, reverse_idx in enumerate(reversed(range(len(self.grid)))):
            forward_diagonal.append(self.grid[idx][reverse_idx])

        if forward_diagonal[0] is not None and forward_diagonal.count(forward_diagonal[0]) == len(forward_diagonal):
            winner = forward_diagonal[0]
            return Player(winner)

        backward_diagonal = []
        for ix in range(len(self.grid)):
            backward_diagonal.append(self.grid[ix][ix])

        if backward_diagonal[0] is not None and backward_diagonal.count(backward_diagonal[0]) == len(backward_diagonal):
            winner = backward_diagonal[0]
            return Player(winner)

    def __str__(self) -> str:
        b = [[' ' if x is None else x for x in c] for c in self.grid]
        d = "\n".join([str(row) for row in b])
        return d
