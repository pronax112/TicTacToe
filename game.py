# Tic Tac Toe game

def print_board(board):
    """
    Prints the current state of the board.
    """
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |")

def get_player_move(player):
    """
    Prompts the player for their move and returns the position on the board.
    """
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        if move < 1 or move > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        return move - 1

def check_win(board):
    """
    Checks if a player has won the game.
    """
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6] # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False

def check_tie(board):
    """
    Checks if the game is tied.
    """
    for i in board:
        if i == " ":
            return False
    return True

def play_game():
    """
    Plays a game of Tic Tac Toe.
    """
    print("Welcome to Tic Tac Toe!")
    board = [" "] * 9
    player = "X"
    print_board(board)
    while True:
        move = get_player_move(player)
        if board[move] == " ":
            board[move] = player
            print_board(board)
            if check_win(board):
                print(f"Player {player} wins!")
                return
            if check_tie(board):
                print("The game is tied!")
                return
            player = "O" if player == "X" else "X"
        else:
            print("That position is already taken. Please choose another.")

play_game()
