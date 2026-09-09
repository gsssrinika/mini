import math
AI = 'O'
HUMAN = 'X'
def print_board(board):
for i in range(0, 9, 3):
print(' | '.join(board[i:i+3]))
if i < 6:
print('---------')
def check_winner(board):
wins = [(0,1,2),(3,4,5),(6,7,8), # rows
(0,3,6),(1,4,7),(2,5,8), # columns
(0,4,8),(2,4,6)] # diagonals
for a, b, c in wins:
if board[a] != ' ' and board[a] == board[b] == board[c]:
return board[a]
if ' ' not in board:
return 'Draw'
return None
def available_moves(board):
return [i for i, cell in enumerate(board) if cell == ' ']
def minimax(board, is_maximizing):
winner = check_winner(board)
if winner == AI:
return 1
if winner == HUMAN:
return -1
if winner == 'Draw':
return 0
if is_maximizing:
best_score = -math.inf
for move in available_moves(board):
board[move] = AI
score = minimax(board, False)
board[move] = ' '
best_score = max(best_score, score)
return best_score
else:
best_score = math.inf
for move in available_moves(board):
board[move] = HUMAN
score = minimax(board, True)
board[move] = ' '
best_score = min(best_score, score)
return best_score
def best_move(board):
best_score = -math.inf

move_choice = None
for move in available_moves(board):
board[move] = AI
score = minimax(board, False)
board[move] = ' '
if score > best_score:
best_score = score
move_choice = move
return move_choice, best_score
# Sample game state: X has taken corners, O (AI) must respond
board = ['X', ' ', ' ',
' ', 'O', ' ',
' ', ' ', 'X']
print('Initial Board:')
print_board(board)
move, score = best_move(board)
board[move] = AI
print('\nAI (O) selects position:', move, ' | Evaluation score:', score)
print('\nBoard after AI move:')
print_board(board)
