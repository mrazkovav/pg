from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.

        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """Vrací všechny možné pohyby figurky."""
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'




class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        if self.color == "white":
            move = (row + 1, col)
        else:  # black
            move = (row - 1, col)

        if self.is_position_on_board(move):
            moves.append(move)

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'




class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for dr, dc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'




class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'




class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for dr, dc in directions:
            for step in range(1, 8):
                move = (row + dr * step, col + dc * step)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'




class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                move = (row + dr, col + dc)
                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'

if __name__ == "__main__":
    pawn = Pawn("white", (2, 2))
    bishop = Bishop("black", (4, 4))
    rook = Rook("white", (1, 1))
    queen = Queen("black", (5, 5))
    king = King("white", (8, 8))

    pieces = [pawn, bishop, rook, queen, king]

    for piece in pieces:
        print(piece)
        print("Possible moves:", piece.possible_moves())
        print()
