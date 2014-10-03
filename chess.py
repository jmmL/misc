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
        for i in all_pieces:
            for j in i:
                for x in range(board_size):
                    for y in range(board_size):
                        if j.row == x and j.column == y:
                            board[x][y] = j.name
        for i in range(board_size):
            print(board[i])
    
    class Piece:
        def __init__(self,name,row,column,proposed_row,proposed_column,colour,):
            self.name = name
            self.row= row
            self.column = column
            self.colour = colour
    
    def create_pawns():
        for i in range(board_size):
            w_pawn.append(Piece("P",6,i,0,0,"white",))
            board[w_pawn[i].row][w_pawn[i].column] = w_pawn[i].name
        for i in range(board_size):
            b_pawn.append(Piece("p",1,i,0,0,"black",))
            board[b_pawn[i].row][b_pawn[i].column] = b_pawn[i].name
        
    def move_piece():
        user_choice = input("Choose a piece (row,column)")
        move_piece_located_at = [0,0]
        move_piece_located_at[0] = int(user_choice[0])
        move_piece_located_at[1] = int(user_choice[2])
        # we only want to "blank" this tile IF we end up moving the piece per move_legality()
        board[move_piece_located_at[0]][move_piece_located_at[1]] = "-"
        print(move_piece_located_at[0], ",", move_piece_located_at[1])
        user_move = input("Choose where to move the piece (row,column)")
        move_piece_to = [0,0]
        move_piece_to[0] = int(user_move[0])
        move_piece_to[1] = int(user_move[2])
        for i in all_pieces:
            for j in i:
                if j.row == move_piece_located_at[0] and j.column == move_piece_located_at[1]:
                    j.proposed_row = move_piece_to[0]
                    j.proposed_column = move_piece_to[1]
                    
    def move_legality(piece):
        if piece.name == "b" or piece.name == "B":
            if diagonal_move_legality(piece):
                return True
        if piece.name == "r" or piece.name == "R":
            if lateral_move_legality(piece):                
                return True
        if piece.name == "q" or piece.name == "Q":
            if lateral_move_legality(piece) or diagonal_move_legality(piece):
                # If the queen behaves like either a bishop or a rook, return true
                return True
    
    # Problems here with move_piece_to and move_piece_located_at?
    # create something like piece.proposed_row, piece.proposed_column
    def diagonal_move_legality(piece):
        if abs(piece.row - piece.proposed_row) == abs(piece.column - piece.proposed_column):
                # A bishop has to move along diagonals, so the abs deltaX and the abs deltaY should be equal
                return True
                
    def lateral_move_legality(piece):
        if ((piece.row - piece.proposed_row == 0) and (abs(piece.column - piece.proposed_column) > 0)) or
             ((abs(piece.row - piece.proposed_row) > 0) and (piece.column - piece.proposed_column == 0)):
            # A rook moves either along a row or a column, but not both
            return True
    create_pawns()
    move_piece()
    print_board()

if __name__ == "__main__":
    main()
