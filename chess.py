def main():
    """ A simple game of chess
    TODO:
            check for check
            add win conditions
            restrict each side to only being able to move pieces of their own colour
            handle user input more elegantly
            handle bad user input (i.e., non-ints, or giving coordinates not on the board)
            add special cases (castling, promotion, en passant)

            bugs: currently valid to select a square of the board with no pieces on it
    """
    import sys
    import math

    board_size = 8
    empty_square = "-"
    move_piece_located_at = [0,0]
    move_piece_to = [0,0]
    game_over = False
    turn_counter = 1
    pieces_in_play = []
    captured_pieces = []
    board = [[empty_square for j in range(board_size)] for i in range(board_size)]

    def update_board():
        """ check if there is a piece located at each square on the board. if there is, add the piece's icon there """
        for piece in pieces_in_play:
            for row in range(board_size):
                for column in range(board_size):
                    if piece.row == row and piece.column == column:
                        board[row][column] = piece.icon
        print_board()

    def print_board():
        """ prints out the board 1 row at a time, with row and column numbering """
        for row in range(board_size):
            print(row, end = " ")
            for column in range(board_size):
                print(board[row][column], end = " ")
            print()
        print(" ", end = " ")
        for column in range(board_size):
            print(column, end = " ")
        print()

    def piece_on_square(row,column):
        """ if there is a piece on the square of the board, return true """

        for piece in pieces_in_play:
            if piece.row == row and piece.column == column:
                return True
        else:
            return False


    def get_piece_on_square(row, column):
        """ returns piece on a particular square """
        # need to reuse this more often

        for piece in pieces_in_play:
            if piece.row == row and piece.column == column:
                return piece


    def capture_piece(row,column):
        """ finds the piece to be captured, removes it from play, and places it in another list for easy printing later on """
        # needs checks for colours!!
        # needs exception for kings!!

        piece = get_piece_on_square(row, column)
        captured_pieces.append(piece)
        pieces_in_play.remove(piece)
        print("Captured ", captured_pieces[-1].icon)


    class Piece:
        def __init__(self,name,colour,icon,row,column,proposed_row,proposed_column,):
            self.name = name
            self.colour = colour
            self.icon = icon
            self.row = row
            self.column = column
            self.proposed_row = proposed_row
            self.proposed_column = proposed_column

    def create_pawns():
        for i in range(board_size):
            pieces_in_play.append(Piece("pawn","white","♙",6,i,0,0,))
            pieces_in_play.append(Piece("pawn","black","♟",1,i,0,0,))

    def create_other_pieces():
        for i in range(2):
            pieces_in_play.append(Piece("rook","white","♖",7,0 + (i * (board_size - 1)),0,0,))
            pieces_in_play.append(Piece("rook","black","♜",0,0 + (i * (board_size - 1)),0,0,))
            pieces_in_play.append(Piece("knight","white","♘",7,1 + (i * (board_size - 3)),0,0,))
            pieces_in_play.append(Piece("knight","black","♞",0,1 + (i * (board_size - 3)),0,0,))
            pieces_in_play.append(Piece("bishop","white","♗",7,2 + (i * (board_size - 5)),0,0,))
            pieces_in_play.append(Piece("bishop","black","♝",0,2 + (i * (board_size - 5)),0,0,))

    def create_royalty():
        pieces_in_play.append(Piece("king","white","♔",7,4,0,0,))
        pieces_in_play.append(Piece("king","black","♚",0,4,0,0,))
        pieces_in_play.append(Piece("queen","white","♕",7,3,0,0,))
        pieces_in_play.append(Piece("queen","black","♛",0,3,0,0,))

    def create_pieces():
        create_pawns()
        create_other_pieces()
        create_royalty()

    def move_piece():
        get_user_input()
        piece = get_piece_on_square(move_piece_located_at[0], move_piece_located_at[1])
        piece.proposed_row = move_piece_to[0]
        piece.proposed_column = move_piece_to[1]
        if move_legal(piece) and not collision_detected(piece):
            # make the old location of the piece blank
            board[piece.row][piece.column] = empty_square
            if piece_on_square(piece.proposed_row,piece.proposed_column):
                capture_piece(piece.proposed_row,piece.proposed_column)
            piece.row = piece.proposed_row
            piece.column = piece.proposed_column
        else:
            print("Sorry, that move is invalid")
            move_piece()

    def get_user_input():
        """ takes user input in x,y format. doesn't currently validate the string supplied """
        user_choice = input("Choose a piece (row,column)")
        if "quit" in user_choice.lower():
            sys.exit("Exiting...")
        move_piece_located_at[0] = int(user_choice[0])
        move_piece_located_at[1] = int(user_choice[2])
        user_move = input("Choose where to move the piece (row,column)")
        if "quit" in user_move.lower():
            sys.exit("Exiting...2")
        move_piece_to[0] = int(user_move[0])
        move_piece_to[1] = int(user_move[2])

    def move_legal(piece):
        if piece.name == "bishop":
            return diagonal_move_legal(piece)
        elif piece.name == "rook":
            return lateral_move_legal(piece)
        elif piece.name == "queen":
            # If the queen behaves like either a bishop or a rook, return true
            return (lateral_move_legal(piece) or diagonal_move_legal(piece))
        elif piece.name == "pawn":
            return pawn_move_legal(piece)
        elif piece.name == "knight":
            return knight_move_legal(piece)
        elif piece.name == "king":
            return king_move_legal(piece)
        else:
            return False


    def diagonal_move_legal(piece):
        """ A bishop has to move along diagonals, so the abs deltaX and the abs deltaY should be equal """
        if abs(piece.row - piece.proposed_row) == abs(piece.column - piece.proposed_column):
            return True

    def lateral_move_legal(piece):
        """ A rook moves either along a row or a column, but not both """
        if ((piece.row - piece.proposed_row == 0) and (abs(piece.column - piece.proposed_column) > 0)) or ((abs(piece.row - piece.proposed_row) > 0) and (piece.column - piece.proposed_column == 0)):
            return True

    def pawn_move_legal(piece):
        # could probably get rid of black/white checking with some additional maths. not sure if worth it
        if piece.colour == "black":
            if piece.row == 1 and piece.proposed_row == 3 and piece.column == piece.proposed_column:
                # collision code
                if (not piece_on_square(2,piece.column)) or (not piece_on_square(3,piece.column)):
                    return True
            elif piece.row == piece.proposed_row - 1 and piece.column == piece.proposed_column:
                if (not piece_on_square(piece.proposed_row,piece.proposed_column)):
                    return True
            elif piece.row == piece.proposed_row - 1 and abs(piece.column - piece.proposed_column) == 1:
                # we're capturing a piece here
                # and sort of doing collision detection. may want to re-think structure
                if piece_on_square(piece.proposed_row,piece.proposed_column) and get_piece_on_square(piece.proposed_row, piece.proposed_column).colour != piece.colour:
                    return True
            else:
                return False

        elif piece.colour == "white":
            if piece.row == 6 and piece.proposed_row == 4 and piece.column == piece.proposed_column:
                if (not piece_on_square(5,piece.column)) or (not piece_on_square(4,piece.column)):
                    return True
            elif piece.row == piece.proposed_row + 1 and piece.column == piece.proposed_column:
                if (not piece_on_square(piece.proposed_row,piece.proposed_column)):
                    return True
            elif piece.row == piece.proposed_row + 1 and abs(piece.column - piece.proposed_column) == 1:
                if piece_on_square(piece.proposed_row,piece.proposed_column) and get_piece_on_square(piece.proposed_row, piece.proposed_column).colour != piece.colour:
                    return True
            else:
                return False

    def knight_move_legal(piece):
        if (abs(piece.row - piece.proposed_row) == 2 and abs(piece.column - piece.proposed_column) == 1) or (abs(piece.row - piece.proposed_row) == 1 and abs(piece.column - piece.proposed_column) == 2):
            return True
        else:
            return False

    def king_move_legal(piece):
        if (abs(piece.row - piece.proposed_row) == 1 and abs(piece.column - piece.proposed_column) == 0) or (abs(piece.row - piece.proposed_row) == 1 and abs(piece.column - piece.proposed_column) == 1) or (abs(piece.row - piece.proposed_row) == 0 and abs(piece.column - piece.proposed_column) == 1):
            return True
        else:
            return False

    def collision_detected(piece):
        # want to check all squares between start and finish - 1
        # also check final square to see if piece is of SAME colour and return False
        # pawn collision currently implemented in pawn_move_legal()
        if piece.name == "rook":
            return rook_collision_detected(piece)
        elif piece.name == "bishop":
            return bishop_collision_detected(piece)
        elif piece.name == "queen":
            # queens behave either as rooks or bishops
            return (rook_collision_detected(piece) or bishop_collision_detected(piece))
        elif piece.name == "knight":
            # knights only care about the square they land on
            return landing_square_collision_detected(piece)
        elif piece.name == "king":
            # kings care about the square they land on, and not moving into check
            # checking for check is not currently implemented
            return landing_square_collision_detected(piece)
        else:
            return False

    def rook_collision_detected(piece):
        # might be able to use max() and min() here rather than .copysign(). not sure if that would come in handy for bishop collision detection
        signed_step_column = int(math.copysign(1,piece.proposed_column - piece.column))
        signed_step_row = int(math.copysign(1,piece.proposed_row - piece.row))

        # check all the squares between start and destination (exclusive). return True if any piece is on these squares
        if piece.row - piece.proposed_row == 0:
            for column in range(piece.column + signed_step_column, piece.proposed_column, signed_step_column):
                if piece_on_square(piece.row, column):
                    return True
        elif piece.column - piece.proposed_column == 0:
            for row in range(piece.row + signed_step_row, piece.proposed_row, signed_step_row):
                if piece_on_square(row, piece.column):
                    return True
        else:
            landing_square_collision_detected(piece)


    def bishop_collision_detected(piece):
        signed_step_column = int(math.copysign(1,piece.proposed_column - piece.column))
        signed_step_row = int(math.copysign(1,piece.proposed_row - piece.row))
        
        for row in range(piece.row + signed_step_row, piece.proposed_row, signed_step_row):
            for column in range(piece.column + signed_step_column, piece.proposed_column, signed_step_column):
                if abs(piece.row - row) == abs(piece.column - column):
                    if piece_on_square(row, column):
                        return True
        else:
            landing_square_collision_detected(piece)
   
            
    def landing_square_collision_detected(piece):
        if not piece_on_square(piece.proposed_row, piece.proposed_column):
            return False
        # allow movement to a square only with a piece of opposite colour on it
        # need to check for kings here
        elif get_piece_on_square(piece.proposed_row, piece.proposed_column).colour != piece.colour:
            return False
        else:
            return True

    print("Remember to set your terminal to black text on a white background!\n")
    create_pieces()
    update_board()

    while not game_over:
        if turn_counter % 2 == 1:
            print("White's turn")
        else:
            print("Black's turn")
        move_piece()
        update_board()
        turn_counter += 1

if __name__ == "__main__":
    main()
