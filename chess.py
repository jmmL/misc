def main():
    """ A simple game of chess
    TODO:
            check for move legality
            check for pieces passing through other pieces
            alternate between black and white
            create non-pawn pieces
            make pieces in a better way
            handle user input more elegantly
            add win conditions
            add special moves (castling...)
            special cases (promoted pawn)
            output board in prettier way
    """
    board_size = 8
    board = [["-" for j in range(board_size)] for i in range(board_size)]
    
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
    
    def print_board():
        for type_of_piece in all_pieces:
            for piece in type_of_piece:
                for row in range(board_size):
                    for column in range(board_size):
                        if piece.row == row and piece.column == column:
                            board[row][column] = piece.icon
        for i in range(board_size):
            print(board[i])
    
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
        for i in range(board_size):
            b_pawn.append(Piece("pawn","black","♟",1,i,0,0,))
        
    def move_piece():
        user_choice = input("Choose a piece (row,column)")
        move_piece_located_at = [0,0]
        move_piece_located_at[0] = int(user_choice[0])
        move_piece_located_at[1] = int(user_choice[2])
        user_move = input("Choose where to move the piece (row,column)")
        move_piece_to = [0,0]
        move_piece_to[0] = int(user_move[0])
        move_piece_to[1] = int(user_move[2])
        for type_of_piece in all_pieces:
            for piece in type_of_piece:
                if piece.row == move_piece_located_at[0] and piece.column == move_piece_located_at[1]:
                    piece.proposed_row = move_piece_to[0]
                    piece.proposed_column = move_piece_to[1]
                    ## Add "collision" detection
                    if move_legality(piece):
                        # blank old location
                        board[piece.row][piece.column] = "-"
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
            ###
            return True
        elif piece.name == "knight":
            ###
            return True
        elif piece.name == "king":
            ###
            return True
            
    
    def diagonal_move_legality(piece):
        # A bishop has to move along diagonals, so the abs deltaX and the abs deltaY should be equal
        if abs(piece.row - piece.proposed_row) == abs(piece.column - piece.proposed_column):
                return True
                
    def lateral_move_legality(piece):
        # A rook moves either along a row or a column, but not both
        if ((piece.row - piece.proposed_row == 0) and (abs(piece.column - piece.proposed_column) > 0)) or ((abs(piece.row - piece.proposed_row) > 0) and (piece.column - piece.proposed_column == 0)):
            return True
    
    create_pawns()
    move_piece()
    print_board()

if __name__ == "__main__":
    main()
