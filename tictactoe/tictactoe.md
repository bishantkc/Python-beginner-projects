# TicTacToe

Tic Tac Toe is a simple two-player game where the objective is to get three of your symbols (usually "X" or "O") in a row on a 3x3 grid. The grid starts empty and players take turns placing their symbol in an empty cell. The game continues until one player successfully gets three of their symbols in a row horizontally, vertically, or diagonally, or until the grid is full, resulting in a draw.

[TicTacToe Documentation](https://github.com/bishantkc/Python-beginner-projects/blob/main/tic_tac_toe.py)

Instruction for creating tictactoe in Python.

**Table of Contents:**

1. [Importing necessary modules](#Importing-necessary-modules)
2. [Defining the Player class](#defining-the-player-class)
3. [Defining the TicTacToe class](#defining-the-tictactoe-class)
4. [Function to play the game](#function-to-play-the-game)
5. [Main block to run the game](#main-block-to-run-the-game)

## Importing necessary modules
```py 
import math
import random
```

## Defining the Player class
```py
class player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

# Creating computer player
class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

# Creating Human player
class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input   move (0-8): ")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again. ")

        return val
```
## Defining the TicTacToe class
```py
class TicTacToe:
    def __init__(self):
        # Using a single list to represent a 3x3 board
        self.board = [" " for _ in range(9)]  
        self.current_winner = None 

    def print_board(self):
        # Displaying the rows of the board
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def print_board_nums(self):
        # Displaying the board with numbers corresponding to each box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        # Showing available moves to players
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        # Number of available moves
        return len(self.available_moves())  

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_index = square // 3
        row = self.board[row_index * 3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_index = square % 3
        column = [self.board[col_index + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
```

## Function to play the game
```py
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"

    # Making moves and deciding winner
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter

            # Switching players
            letter = "O" if letter == "X" else "X" 

        # Tiny break after each step
        time.sleep(0.8)  

    if print_game:
        print("It's a tie!")
```

## Main block to run the game
```py
if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
```