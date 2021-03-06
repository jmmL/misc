#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""A simple game of chess"""
# TODO:   check for check
#         add win conditions
#         restrict each side to only being able to move pieces of their own colour
#         handle user input more elegantly
#         handle bad user input (i.e., non-ints, or giving coordinates not on the board)
#         add special cases (castling, promotion, en passant)
#         write unit tests
#
#         bugs: currently valid to select a square of the board with no pieces on it

import sys

board_size = 8
empty_square = "-"
pieces_in_play = []
captured_pieces = []
board = [[empty_square for j in range(board_size)] for i in range(board_size)]

black_base_starting_row = 0
black_pawn_starting_row = 1
white_base_starting_row = 7
white_pawn_starting_row = 6

queen_starting_column = 3
king_starting_column = 4

black_move_direction = 1
white_move_direction = -1


class Piece:
    """Most pieces are initialised with only a colour and a column.
    The attributes row and column that correspond to their
    current location, and the attributes proposed_row and proposed_column
    correspond to coordinates of their proposed move (and are initialised at 0,0)
    """
    proposed_row = 0
    proposed_column = 0

    def __init__(self, colour, row, column,):
        self.colour = colour
        self.icon = "P"
        self.row = row
        self.column = column

    def proposed_square_is_empty_or_capturable(self):
        """Determines whether there is a piece on the final square of the move,
        and allows the move only if the piece is of the opposite colour. Does
        not currently allow for check."""
        if not piece_on_square(self.proposed_row, self.proposed_column):
            return True
        # allow movement to a square only with a piece of opposite colour on it
        # need to check for kings here
        elif get_piece_on_square(self.proposed_row, self.proposed_column).colour != self.colour:
            return True
        else:
            return False

    def diagonal_move_legal(self):
        """A bishop has to move along diagonals, so the abs deltaX and the abs deltaY should be equal."""
        if abs(self.row - self.proposed_row) == abs(self.column - self.proposed_column):
            return True

    def straight_move_legal(self):
        """A rook moves either along a row or a column, but not both."""
        if (self.row - self.proposed_row == 0) and (abs(self.column - self.proposed_column) > 0):
            return True
        elif (abs(self.row - self.proposed_row) > 0) and (self.column - self.proposed_column == 0):
            return True
        else:
            return False

    def diagonal_path_is_clear(self):
        """Checks for bishop collision, taking into account that they can move in
        one of four directions"""
        move_direction_column = get_move_direction(self.proposed_column, self.column)
        move_direction_row = get_move_direction(self.proposed_row, self.row)

        # TODO: search the path more efficiently / make more readable
        for row in range(self.row + move_direction_row, self.proposed_row, move_direction_row):
            for column in range(self.column + move_direction_column, self.proposed_column, move_direction_column):
                if abs(self.row - row) == abs(self.column - column):
                    if piece_on_square(row, column):
                        return False
        else:
            return True

    def straight_path_is_clear(self):
        """Checks for rook collisions, taking into account that they can move in
        one of four directions"""

        if self.row == self.proposed_row:
            move_direction = get_move_direction(self.proposed_column, self.column)
            start_of_path = self.column + move_direction

            for column in range(start_of_path, self.proposed_column, move_direction):
                if piece_on_square(self.row, column):
                    return False
            return True

        elif self.column == self.proposed_column:
            move_direction = get_move_direction(self.proposed_row, self.row)
            start_of_path = self.row + move_direction

            for row in range(start_of_path, self.proposed_row, move_direction):
                if piece_on_square(row, self.column):
                    return False
            return True

        else:
            # This is never hit when called on a straight path!
            # Throw exception perhaps?
            return False


class Pawn(Piece):
    def __init__(self, colour, column,):
        self.colour = colour
        self.icon = self.get_icon()
        self.row = self.starting_row()
        self.column = column

    def get_icon(self):
        if self.colour == "black":
            return "♟"
        else:
            return "♙"

    def starting_row(self):
        if self.colour == "black":
            return black_pawn_starting_row
        else:
            return white_pawn_starting_row

    def move_direction(self):
        if self.colour == "black":
            return black_move_direction
        else:
            return white_move_direction

    def move_is_legal(self):
        """Determines legality of pawn moves, taking into account their ability to
        move two rows from their starting square and their need to move diagonally
        to capture a piece. Does not currently handle en passant or promotion."""
        # collision code
        if self.double_row_move() and self.path_is_clear():
            return True
        # collision code
        elif self.single_row_move() and self.path_is_clear():
            return True
        elif self.diagonal_move() and self.capturing_piece():
            return True
        else:
            return False

    def double_row_move(self):
        if self.row == self.starting_row() and self.proposed_row == self.starting_row() + (2 * self.move_direction()) and self.column == self.proposed_column:
            return True
        else:
            return False

    def single_row_move(self):
        if self.row == self.proposed_row - (1 * self.move_direction()) and self.column == self.proposed_column:
            return True
        else:
            return False

    def diagonal_move(self):
        if self.row == self.proposed_row - (1 * self.move_direction()) and abs(self.column - self.proposed_column) == 1:
            return True
        else:
            return False

    def path_is_clear(self):
        start_of_path = self.row + (1 * self.move_direction())
        end_of_path = self.proposed_row + (1 * self.move_direction())

        for row in range(start_of_path, end_of_path, self.move_direction()):
            if piece_on_square(row, self.column):
                return False
        return True

    def capturing_piece(self):
        if piece_on_square(self.proposed_row, self.proposed_column) and self.proposed_square_is_empty_or_capturable():
            return True
        else:
            return False


class Rook(Piece):
    def __init__(self, colour, column):
        self.colour = colour
        self.icon = self.get_icon()
        self.row = self.starting_row()
        self.column = column

    def starting_row(self):
        if self.colour == "black":
            return black_base_starting_row
        else:
            return white_base_starting_row

    def get_icon(self):
        if self.colour == "black":
            return "♜"
        else:
            return "♖"

    def move_is_legal(self):
        return self.straight_move_legal() and self.straight_path_is_clear() and self.proposed_square_is_empty_or_capturable()


class Knight(Piece):
    def __init__(self, colour, column):
        self.colour = colour
        self.icon = self.get_icon()
        self.row = self.starting_row()
        self.column = column

    def starting_row(self):
        if self.colour == "black":
            return black_base_starting_row
        else:
            return white_base_starting_row

    def get_icon(self):
        if self.colour == "black":
            return "♞"
        else:
            return "♘"

    def move_is_legal(self):
        if self.move_is_L_shape() and self.proposed_square_is_empty_or_capturable():
            return True
        else:
            return False

    def move_is_L_shape(self):
        """Determines knight move legality"""
        if abs(self.row - self.proposed_row) == 2 and abs(self.column - self.proposed_column) == 1:
            return True
        elif abs(self.row - self.proposed_row) == 1 and abs(self.column - self.proposed_column) == 2:
            return True
        else:
            return False


class Bishop(Piece):
    def __init__(self, colour, column):
        self.colour = colour
        self.icon = self.get_icon()
        self.row = self.starting_row()
        self.column = column

    def starting_row(self):
        if self.colour == "black":
            return black_base_starting_row
        else:
            return white_base_starting_row

    def get_icon(self):
        if self.colour == "black":
            return "♝"
        else:
            return "♗"

    def move_is_legal(self):
        return self.diagonal_move_legal() and self.diagonal_path_is_clear() and self.proposed_square_is_empty_or_capturable()


class Queen(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.icon = self.get_icon()
        self.row = self.starting_row()
        self.column = queen_starting_column

    def starting_row(self):
        if self.colour == "black":
            return black_base_starting_row
        else:
            return white_base_starting_row

    def get_icon(self):
        if self.colour == "black":
            return "♛"
        else:
            return "♕"

    def move_is_legal(self):
        if (self.diagonal_move_legal() and self.diagonal_path_is_clear) or (self.straight_move_legal() and self.straight_path_is_clear()):
            return self.proposed_square_is_empty_or_capturable()
        else:
            return False


class King(Piece):
    def __init__(self, colour):
        self.colour = colour
        self.icon = self.get_icon()
        self.row = self.starting_row()
        self.column = king_starting_column

    def starting_row(self):
        if self.colour == "black":
            return black_base_starting_row
        else:
            return white_base_starting_row

    def get_icon(self):
        if self.colour == "black":
            return "♚"
        else:
            return "♔"

    def move_is_legal(self):
        return self.move_is_only_one_square() and self.proposed_square_is_empty_or_capturable()

    def move_is_only_one_square(self):
        """Determines king move legality. The check status of the king is not
        currently taken into account"""
        if abs(self.row - self.proposed_row) == 1 and abs(self.column - self.proposed_column) == 0:
            return True
        elif abs(self.row - self.proposed_row) == 1 and abs(self.column - self.proposed_column) == 1:
            return True
        elif abs(self.row - self.proposed_row) == 0 and abs(self.column - self.proposed_column) == 1:
            return True
        else:
            return False


def update_board():
    """For each piece in play, add the piece's icon to the piece's coordinates on the board"""
    for piece in pieces_in_play:
        board[piece.row][piece.column] = piece.icon


def print_board():
    """Prints out the board 1 square at a time, with row and column numbering"""
    for row in range(board_size):
        print(row, end=" ")
        for column in range(board_size):
            print(board[row][column], end=" ")
        print()
    print(" ", end=" ")
    for column in range(board_size):
        print(column, end=" ")
    print()


def piece_on_square(row, column):
    """If there is a piece on the square of the board, return true"""
    for piece in pieces_in_play:
        if piece.row == row and piece.column == column:
            return True
    else:
        return False


def get_piece_on_square(row, column):
    """Returns piece on a particular square """
    for piece in pieces_in_play:
        if piece.row == row and piece.column == column:
            return piece


def capture_piece(piece):
    """Removes piece from play, and places it in a list of captured pieces for easy printing later on"""
    # needs checks for colours!!
    # needs exception for kings!!
    captured_pieces.append(piece)
    pieces_in_play.remove(piece)
    print("Captured %s" % captured_pieces[-1].icon)


def get_move_direction(proposed, current):
    """Gets the direction that the piece is moving in across the board: 1 if it is going from low to high, or -1 if
    going from high to low
    """
    if proposed > current:
        return 1
    elif proposed < current:
        return -1
    else:
        # This should never happen
        return 0


def create_pawns():
    """Places two rows of pawns; one for each colour"""
    for column in range(board_size):
        pieces_in_play.append(Pawn("white", column))
        pieces_in_play.append(Pawn("black", column))


def create_other_pieces():
    """Places all pieces which appear twice on the board. Their placement is
    mirrored across the columns of the board"""
    for i in range(2):
        pieces_in_play.append(Rook("white", 0 + (i * (board_size - 1))))
        pieces_in_play.append(Rook("black", 0 + (i * (board_size - 1))))
        pieces_in_play.append(Knight("white", 1 + (i * (board_size - 3))))
        pieces_in_play.append(Knight("black", 1 + (i * (board_size - 3))))
        pieces_in_play.append(Bishop("white", 2 + (i * (board_size - 5))))
        pieces_in_play.append(Bishop("black", 2 + (i * (board_size - 5))))


def create_royalty():
    """Places kings and queens in pre-determined squares"""
    pieces_in_play.append(King("white"))
    pieces_in_play.append(King("black"))
    pieces_in_play.append(Queen("white"))
    pieces_in_play.append(Queen("black"))


def create_pieces():
    """Calls all the functions required to populate the board"""
    create_pawns()
    create_other_pieces()
    create_royalty()


def set_new_piece_position(piece):
    piece.row = piece.proposed_row
    piece.column = piece.proposed_column


def clear_old_board_position(piece):
    board[piece.row][piece.column] = empty_square


def move_piece():
    """Decides whether or not to move the piece, based on the coordinates
    inputted by the user and the .move_is_legal() method of the piece. In the future,
    this will also depend on a check_for_check function.
    If a move is made then the old square is made empty"""
    user_input = get_user_input()
    piece = get_piece_on_square(user_input[0][0], user_input[0][1])

    piece.proposed_row = user_input[1][0]
    piece.proposed_column = user_input[1][1]

    if piece.move_is_legal():
        if piece_on_square(piece.proposed_row, piece.proposed_column):
            piece_to_capture = get_piece_on_square(piece.proposed_row, piece.proposed_column)
            capture_piece(piece_to_capture)

        clear_old_board_position(piece)
        set_new_piece_position(piece)

    else:
        print("Sorry, that move is invalid")
        move_piece()


def get_user_input():
    """Takes user input, assuming a "x,y" format. Stores the 4 coordinates in a list"""
    # TODO: validate input

    starting_square = input("Choose a piece (row,column)")
    if "quit" in starting_square.lower():
        sys.exit("Exiting...")

    finishing_square = input("Choose where to move the piece (row,column)")
    if "quit" in finishing_square.lower():
        sys.exit("Exiting...2")

    user_input = [[0, 0], [0, 0]]

    starting_square = starting_square.split(",")
    finishing_square = finishing_square.split(",")

    user_input[0][0] = int(starting_square[0])
    user_input[0][1] = int(starting_square[1])
    user_input[1][0] = int(finishing_square[0])
    user_input[1][1] = int(finishing_square[1])

    return user_input


def announce_to_players(turn_counter):
    if turn_counter % 2 == 1:
        print("White's turn")
    else:
        print("Black's turn")


def main():
    """Calls the relevant functions to set up the board, and then loops each move
    of the game. Win conditions are not currently implemented."""
    game_over = False
    turn_counter = 1
    print("Remember to set your terminal to black text on a white background!\n")
    create_pieces()
    update_board()
    print_board()

    while not game_over:
        announce_to_players(turn_counter)
        move_piece()
        update_board()
        print_board()
        turn_counter += 1


if __name__ == "__main__":
    main()
