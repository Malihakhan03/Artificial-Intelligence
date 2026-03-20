import math

# Initialize board
board = [' ' for _ in range(9)]

# Print board
def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

# Check winner
def check_winner(b):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],   # rows
        [0,3,6],[1,4,7],[2,5,8],   # columns
        [0,4,8],[2,4,6]            # diagonals
    ]
    
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] and b[cond[0]] != ' ':
            return b[cond[0]]
    return None

# Check if board full
def is_full(b):
    return ' ' not in b

# Alpha-Beta Pruning
def alpha_beta(b, depth, is_max, alpha, beta):
    winner = check_winner(b)
    
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_full(b):
        return 0

    if is_max:
        max_eval = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                eval = alpha_beta(b, depth+1, False, alpha, beta)
                b[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break   # Pruning
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                eval = alpha_beta(b, depth+1, True, alpha, beta)
                b[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break   # Pruning
        return min_eval

# Find best move for AI
def best_move():
    best_val = -math.inf
    move = -1
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = alpha_beta(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Game loop
def play():
    print("Tic Tac Toe Game (You = O, AI = X)")
    print_board()
    
    while True:
        # Player move
        pos = int(input("Enter position (0-8): "))
        if board[pos] != ' ':
            print("Invalid move!")
            continue
        
        board[pos] = 'O'
        print_board()
        
        if check_winner(board) or is_full(board):
            break
        
        # AI move
        ai = best_move()
        board[ai] = 'X'
        print("AI played at:", ai)
        print_board()
        
        if check_winner(board) or is_full(board):
            break

    winner = check_winner(board)
    if winner:
        print("Winner:", winner)
    else:
        print("Draw!")

# Run game
play()