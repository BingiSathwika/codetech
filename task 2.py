import math

# Define constants
X = "X"
O = "O"
EMPTY = " "
NUM_SQUARES = 9

# Function to create the board
def create_board():
    return [EMPTY] * NUM_SQUARES

# Function to display the board
def display_board(board):
    print("|---|---|---|")
    for row in range(3):
        print(f"| {board[row * 3]} | {board[row * 3 + 1]} | {board[row * 3 + 2]} |")
        print("|---|---|---|")

# Function to check for a winner
def is_winner(board, player):
    win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6))
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full (no empty spaces)
def is_board_full(board):
    return not any(EMPTY == space for space in board)

# Minimax function to evaluate the best move for the AI
def minimax(board, depth, maximizing_player, alpha, beta):
    # Base cases: terminal state (win, draw, or max depth reached)
    if is_winner(board, X):
        return -10 + depth if maximizing_player else 10 - depth
    elif is_winner(board, O):
        return 10 + depth if maximizing_player else -10 - depth
    elif is_board_full(board):
        return 0

    # Recursive case: evaluate all possible moves
    if maximizing_player:
        value = -math.inf
        for i in range(NUM_SQUARES):
            if board[i] == EMPTY:
                board[i] = X  # Simulate AI's move
                value = max(value, minimax(board, depth + 1, False, alpha, beta))
                board[i] = EMPTY  # Undo the simulated move
                alpha = max(alpha, value)
                if beta <= alpha:
                    break  # Alpha-Beta pruning
        return value
    else:
        value = math.inf
        for i in range(NUM_SQUARES):
            if board[i] == EMPTY:
                board[i] = O  # Simulate human's move
                value = min(value, minimax(board, depth + 1, True, alpha, beta))
                board[i] = EMPTY  # Undo the simulated move
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Alpha-Beta pruning
        return value

# Get the AI's best move using Minimax
def get_ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(NUM_SQUARES):
        if board[i] == EMPTY:
            board[i] = X  # Simulate AI's move
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = EMPTY  # Undo the simulated move
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Function to get player's move
def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and board[move] == EMPTY:
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")

# Main game loop

def main():
    board = create_board()
    current_player = X

    print("Welcome to Tic-Tac-Toe!")
    print("To make a move, enter the number corresponding to the position on the board.")
    print("You are 'X' and the computer is 'O'.")

    while True:
        display_board(board)

        if current_player == X:
            move = human_move(board)
            board[move] = X
            current_player = O
        else:
            # AI's turn (using Minimax with Alpha-Beta pruning)
            move = get_ai_move(board)
            board[move] = O
            current_player = X

        # Check for win or draw
        if is_winner(board, X):
            display_board(board)
            print("X wins!")
            break
        elif is_winner(board, O):
            display_board(board)
            print("O wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("Draw!")
            break

if __name__ == "__main__":
    main()

