"""
A simple, object-oriented Tic-Tac-Toe game with a separate Player class.
"""

class Player:
    """
    Represents a player in the Tic-Tac-Toe game.
    """
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        """Prompts the player for their move."""
        return input(f"Player {self.name} ('{self.symbol}'), enter your move: ")


class TicTacToeGame:
    """
    Encapsulates all the logic and data for a Tic-Tac-Toe game.
    """
    def __init__(self, player1, player2):
        """Initializes the game state with two players."""
        self.board = {}
        self.player1 = player1
        self.player2 = player2
        self.current_player = None
        self.reset_game()

    def reset_game(self):
        """Resets the game board and sets the starting player."""
        self.board = {
            '11': ' ', '12': ' ', '13': ' ',
            '21': ' ', '22': ' ', '23': ' ',
            '31': ' ', '32': ' ', '33': ' '
        }
        self.current_player = self.player1

    def print_board(self):
        """Prints the 3x3 Tic-Tac-Toe board."""
        print("\n")
        print(f" {self.board['11']} | {self.board['12']} | {self.board['13']} ")
        print("---|---|---")
        print(f" {self.board['21']} | {self.board['22']} | {self.board['23']} ")
        print("---|---|---")
        print(f" {self.board['31']} | {self.board['32']} | {self.board['33']} ")
        print("\n")

    def check_win(self):
        """Checks if the current player has won the game."""
        p = self.current_player.symbol
        # Check rows, columns, and diagonals
        return ((self.board['11'] == self.board['12'] == self.board['13'] == p) or
                (self.board['21'] == self.board['22'] == self.board['23'] == p) or
                (self.board['31'] == self.board['32'] == self.board['33'] == p) or
                (self.board['11'] == self.board['21'] == self.board['31'] == p) or
                (self.board['12'] == self.board['22'] == self.board['32'] == p) or
                (self.board['13'] == self.board['23'] == self.board['33'] == p) or
                (self.board['11'] == self.board['22'] == self.board['33'] == p) or
                (self.board['13'] == self.board['22'] == self.board['31'] == p))

    def check_draw(self):
        """Checks if the game is a draw (board is full)."""
        return ' ' not in self.board.values()

    def switch_player(self):
        """Switches the turn to the other player."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def play_game(self):
        """Contains the main loop for a single game session."""
        game_over = False
        while not game_over:
            self.print_board()
            
            # Delegate getting input to the current Player object
            move = self.current_player.get_move()

            if move in self.board and self.board[move] == ' ':
                self.board[move] = self.current_player.symbol
            else:
                print("Invalid move! Either the position is taken or the code is incorrect. Please try again.")
                continue

            if self.check_win():
                self.print_board()
                print(f"🎉 Congratulations! Player {self.current_player.name} ('{self.current_player.symbol}') wins!")
                game_over = True
            elif self.check_draw():
                self.print_board()
                print("It's a draw! The board is full.")
                game_over = True
            else:
                self.switch_player()

def main():
    """
    Main function to run the Tic-Tac-Toe game.
    Manages the game creation and restart loop.
    """
    print("==== Welcome to Object-Oriented Tic-Tac-Toe! ====")
    print("Player A is 'O' and Player B is 'X'.")
    print("Enter your move as a two-digit number (e.g., 11 for top-left, 33 for bottom-right).")
    
    # Create player instances
    player_a = Player("A", "O")
    player_b = Player("B", "X")
    
    # Create a game instance with the players
    game = TicTacToeGame(player_a, player_b)
    
    while True:  # Outer loop for restarting the game
        game.play_game()
        print("\n--- Starting a new game! ---")
        game.reset_game()

if __name__ == "__main__":
    main()
