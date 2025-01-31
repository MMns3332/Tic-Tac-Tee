def print_board(board):
    for row in board:
        print(" | ".join(row))
    print("\n")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    for _ in range(9):
        print_board(board)
        row, col = map(int, input(f"Player {player}, enter row and column (0-2): ").split())
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                return
            player = "O" if player == "X" else "X"
    print("It's a draw!")