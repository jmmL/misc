def main():
    """ An easier version of 2048, called 512. Some behaviour might be different """
    import random
    board_size = 4
    board = [[0 for j in range(board_size)] for i in range(board_size)]

    def print_board():
        for i in range(board_size):
            print(board[i])

    def move_up():
        for k in range(board_size - 1):
            for i in range(1,board_size):
                for j in range(board_size):
                    if board[i-1][j] == 0 and board[i][j] > 0:
                        board[i-1][j] = board[i][j]
                        board[i][j] = 0

    def move_down():
        for k in range(board_size - 1):
            for i in range(0,board_size - 1):
                for j in range(board_size):
                    if board[i+1][j] == 0 and board[i][j] > 0:
                        board[i+1][j] = board[i][j]
                        board[i][j] = 0

    def move_left():
        for k in range(board_size - 1):
            for i in range(board_size):
                for j in range(1,board_size):
                    if board[i][j-1] == 0 and board[i][j] > 0:
                        board[i][j-1] = board[i][j]
                        board[i][j] = 0

    def move_right():
        for k in range(board_size - 1):
            for i in range(board_size):
                for j in range(0,board_size - 1):
                    if board[i][j+1] == 0 and board[i][j] > 0:
                        board[i][j+1] = board[i][j]
                        board[i][j] = 0

    def merge_up():
        for i in range(board_size - 2,-1,-1):
            for j in range(board_size):
                if board[i][j] == board[i+1][j]:
                    board[i][j] *= 2
                    board[i+1][j] = 0

    def merge_down():
        for i in range(1,board_size):
            for j in range(board_size):
                if board[i][j] == board[i-1][j]:
                    board[i][j] *= 2
                    board[i-1][j] = 0

    def merge_left():
        for i in range(board_size):
            for j in range(board_size - 2, -1, -1):
                if board[i][j] == board[i][j+1]:
                    board[i][j] *= 2
                    board[i][j+1] = 0

    def merge_right():
        for i in range(board_size):
            for j in range(1,board_size):
                if board[i][j] == board[i][j-1]:
                    board[i][j] *= 2
                    board[i][j-1] = 0

    def get_player_input():
        player_move = input("Please input a move: ")
        if "q" in player_move:
            print("Quitting")
            game_over = True
        elif "w" in player_move:
            move_up()
            merge_up()
            move_up()
        elif "a" in player_move:
            move_left()
            merge_left()
            move_left()
        elif "d" in player_move:
            move_right()
            merge_right()
            move_right()
        elif "s" in player_move:
            move_down()
            merge_down()
            move_down()
        else:
            print("Move not understood. Please enter q,w,a,s or d")
            get_player_input()

    def place_2():
        random_column = random.randrange(0,board_size)
        random_row = random.randrange(0,board_size)
        if board[random_row][random_column] == 0:
            board[random_row][random_column] = 2
        else:
            place_2()

    def board_full():
        if min(min(i) for i in board) > 0:
            return True
        else:
            return False

    print_board()
    game_over = False

    while not game_over:
        get_player_input()
        if max(max(i) for i in board) == 512:
            print("You won!")
            game_over = True
        elif board_full():
            print("Board is full, exiting")
            game_over = True
        else:
            place_2()
        print_board()

if __name__ == "__main__":
    main()
