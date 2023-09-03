def draw_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
def check_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        draw_board(board)
        row = int(input("Введите номер строки (0, 1 или 2): "))
        col = int(input("Введите номер столбца (0, 1 или 2): "))
        if board[row][col] != " ":
            print("Клетка уже занята. Попробуйте еще раз.")
            continue
        board[row][col] = current_player
        if check_winner(board, current_player):
            draw_board(board)
            print(f"Игрок {current_player} победил!")
            break
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            draw_board(board)
            print("Ничья!")
            break
        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()

