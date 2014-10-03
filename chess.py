def main():
    """ A simple game of chess
    TODO:
            check for collision
            check for check
            add win conditions
            alternate between black and white
            make pieces in a better way
            handle user input more elegantly
            handle bad user input
            add special cases (castling, promotion, en passant)
    """
    import sys
    board_size = 8
    empty_square = "-"
    board = [[empty_square for j in range(board_size)] for i in range(board_size)]
    move_piece_located_at = [0,0]
    move_piece_to = [0,0]

    w_pawn = []
    b_pawn = []
    w_rook = []
    w_bishop = []
    w_knight = []
    w_king = []
    w_queen = []
    b_rook = []
    b_bishop = []
    b_knight = []
    b_king = []
    b_queen = []

    all_pieces = [w_pawn, b_pawn, w_rook, w_bishop, w_knight, w_king,
        w_queen, b_rook, b_bishop, b_knight, b_king, b_queen]

    def update_board():
        for type_of_piece in all_pieces:
            for piece in type_of_piece:
                for row in range(board_size):
                    for column in range(board_size):
                        if piece.row == row and piece.column == column:
                            board[row][column] = piece.icon
        print_board()

    ## probably could use a function "is_piece_on_square" or similar. reuse code from update board in the collision function?

    def print_board():
        for row in range(board_size):
            print(row, end = " ")
            for column in range(board_size):
                print(board[row][column], end = " ")
            print()
        print(" ", end = " ")
        for column in range(board_size):
            print(column, end = " ")
        print()

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
            w_pawn.append(Piece("pawn","white","♙",6,i,0,0,))
            b_pawn.append(Piece("pawn","black","♟",1,i,0,0,))

    def create_other_pieces():
        for i in range(2):
            w_rook.append(Piece("rook","white","♖",7,0 + (i * (board_size - 1)),0,0,))
            b_rook.append(Piece("rook","black","♜",0,0 + (i * (board_size - 1)),0,0,))
            w_knight.append(Piece("knight","white","♘",7,1 + (i * (board_size - 3)),0,0,))
            b_knight.append(Piece("knight","black","♞",0,1 + (i * (board_size - 3)),0,0,))
            w_bishop.append(Piece("bishop","white","♗",7,2 + (i * (board_size - 5)),0,0,))
            b_bishop.append(Piece("bishop","black","♝",0,2 + (i * (board_size - 5)),0,0,))

    def create_royalty():
        w_king.append(Piece("king","white","♔",7,4,0,0,))
        b_king.append(Piece("king","black","♚",0,4,0,0,))
        w_queen.append(Piece("queen","white","♕",7,3,0,0,))
        b_queen.append(Piece("queen","black","♛",0,3,0,0,))

    def create_pieces():
        create_pawns()
        create_other_pieces()
        create_royalty()

    def move_piece():
        user_choice = input("Choose a piece (row,column)")
        if "quit" in user_choice.lower():
            sys.exit("Exiting...")
        #move_piece_located_at = [0,0]
        move_piece_located_at[0] = int(user_choice[0])
        move_piece_located_at[1] = int(user_choice[2])
        user_move = input("Choose where to move the piece (row,column)")
        if "quit" in user_move.lower():
            sys.exit("Exiting...2")
        #move_piece_to = [0,0]
        move_piece_to[0] = int(user_move[0])
        move_piece_to[1] = int(user_move[2])
        for type_of_piece in all_pieces:
            for piece in type_of_piece:
                if piece.row == move_piece_located_at[0] and piece.column == move_piece_located_at[1]:
                    piece.proposed_row = move_piece_to[0]
                    piece.proposed_column = move_piece_to[1]
                    if move_legality(piece) and collision_detection(piece):
                        # blank old location
                        board[piece.row][piece.column] = empty_square
                        piece.row = piece.proposed_row
                        piece.column = piece.proposed_column
                        # Do we need to clear proposed_row and _column here?
                    else:
                        print("Sorry, that move is invalid")
                        move_piece()

    def move_legality(piece):
        if piece.name == "bishop":
            if diagonal_move_legality(piece):
                return True
        elif piece.name == "rook":
            if lateral_move_legality(piece):
                return True
        elif piece.name == "queen":
            # If the queen behaves like either a bishop or a rook, return true
            if lateral_move_legality(piece) or diagonal_move_legality(piece):
                return True
        elif piece.name == "pawn":
            if pawn_move_legality(piece):
                return True
        elif piece.name == "knight":
            if knight_move_legaility(piece):
                return True
        elif piece.name == "king":
            if king_move_legality():
                return True
        else:
            return False


    def diagonal_move_legality(piece):
        # A bishop has to move along diagonals, so the abs deltaX and the abs deltaY should be equal
        if abs(piece.row - piece.proposed_row) == abs(piece.column - piece.proposed_column):
                return True

    def lateral_move_legality(piece):
        # A rook moves either along a row or a column, but not both
        if ((piece.row - piece.proposed_row == 0) and (abs(piece.column - piece.proposed_column) > 0)) or ((abs(piece.row - piece.proposed_row) > 0) and (piece.column - piece.proposed_column == 0)):
            return True

    def pawn_move_legality(piece):
        if piece.colour == "black":
            if piece.row == 1 and piece.proposed_row == 3 and piece.column == piece.proposed_column:
                return True
            elif piece.row == piece.proposed_row - 1 and piece.column == piece.proposed_column:
                return True
            elif piece.row == piece.proposed_row - 1 and abs(piece.column - piece.proposed_column) == 1 and capturing_piece():
                return True
            else:
                return False
        if piece.colour == "white":
            if piece.row == 6 and piece.proposed_row == 4 and piece.column == piece.proposed_column:
                return True
            elif piece.row == piece.proposed_row + 1 and piece.column == piece.proposed_column:
                return True
            elif piece.row == piece.proposed_row + 1 and abs(piece.column - piece.proposed_column) == 1 and capturing_piece():
                return True
            else:
                return False

    def knight_move_legality(piece):
        if (abs(piece.row - piece.proposed_row) == 2 and abs(piece.column - piece.proposed_column) == 1) or (abs(piece.row - piece.proposed_row) == 1 and abs(piece.column - piece.proposed_column) == 2):
            return True
        else:
            return False

    def king_move_legality(piece):
        if (abs(piece.row - piece.proposed_row) == 1 and abs(piece.column - piece.proposed_column) == 0) or (abs(piece.row - piece.proposed_row) == 1 and abs(piece.column - piece.proposed_column) == 1) or (abs(piece.row - piece.proposed_row) == 0 and abs(piece.column - piece.proposed_column) == 1):
            return True
        else:
            return False

    def collision_detection(piece):
        return True

    def capturing_piece():
        return True

    print("Remember to set your terminal to black text on a white background!\n")
    create_pieces()
    update_board()
    game_over = False
    turn_counter = 1
    
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
