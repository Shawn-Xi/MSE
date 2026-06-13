"""tic-tac-toe game"""
def print_board(board):
    """Prints the 3x3 Tic-Tac-Toe board."""
    print("\n")
    print(f" {board['11']} | {board['12']} | {board['13']} ")
    print("---|---|---")
    print(f" {board['21']} | {board['22']} | {board['23']} ")
    print("---|---|---")
    print(f" {board['31']} | {board['32']} | {board['33']} ")
    print("\n")

def check_win(board, player):
    """Checks if the given player has won the game."""
    # Check rows
    if (board['11'] == board['12'] == board['13'] == player or
        board['21'] == board['22'] == board['23'] == player or
        board['31'] == board['32'] == board['33'] == player):
        return True
    # Check columns
    if (board['11'] == board['21'] == board['31'] == player or
        board['12'] == board['22'] == board['32'] == player or
        board['13'] == board['23'] == board['33'] == player):
        return True
    # Check diagonals
    if (board['11'] == board['22'] == board['33'] == player or
        board['13'] == board['22'] == board['31'] == player):
        return True
    return False

def check_draw(board):
    """Checks if the game is a draw (board is full)."""
    for key in board:
        if board[key] == ' ':
            return False
    return True

def main():
    """Main function to run the Tic-Tac-Toe game."""
    print("==== Welcome to Tic-Tac-Toe! ====")
    print("Player A is 'O' and Player B is 'X'.")
    print("Enter your move as a two-digit number (e.g., 11 for top-left, 33 for bottom-right).")

    while True:  # Outer loop for restarting the game
        # 1. & 4. Initialize the board collection
        board = {
            '11': ' ', '12': ' ', '13': ' ',
            '21': ' ', '22': ' ', '23': ' ',
            '31': ' ', '32': ' ', '33': ' '
        }
        current_player_name = "A"
        current_player_symbol = "O"
        game_over = False

        while not game_over:  # Inner loop for a single game
            # 1. Print the map
            print_board(board)

            # 2. Get player input
            move = input(f"Player {current_player_name} ('{current_player_symbol}'), enter your move: ")

            # Validate input
            if move in board and board[move] == ' ':
                board[move] = current_player_symbol
            else:
                print("Invalid move! Either the position is taken or the code is incorrect. Please try again.")
                continue

            # 3. Check for a win
            if check_win(board, current_player_symbol):
                print_board(board)
                print(f"🎉 Congratulations! Player {current_player_name} ('{current_player_symbol}') wins!")
                game_over = True
            # Check for a draw
            elif check_draw(board):
                print_board(board)
                print("It's a draw! The board is full.")
                game_over = True
            else:
                # Switch players
                if current_player_name == "A":
                    current_player_name = "B"
                    current_player_symbol = "X"
                else:
                    current_player_name = "A"
                    current_player_symbol = "O"
        # 5. Restart game
        print("\n--- Starting a new game! ---")
        # The outer loop will now automatically restart

if __name__ == "__main__":
    main()
