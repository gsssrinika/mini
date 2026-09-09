Tic-Tac-Toe AI using Minimax

This project implements a Tic-Tac-Toe game state evaluator and AI player using the Minimax algorithm.

The AI plays as O, while the human player is represented by X. The Minimax algorithm evaluates all possible future moves and selects the move that provides the best possible outcome for the AI.

Features
Implements the classic Tic-Tac-Toe board.
Uses X as the human player.
Uses O as the AI player.
Detects wins, losses, and draws.
Identifies all available moves.
Uses the Minimax algorithm for decision-making.
Calculates an evaluation score for the selected move.
Displays the board before and after the AI's move.
Requirements
Python 3.x
No external libraries are required.

The program uses Python's built-in math module.

Project Structure
.
├── main.py
└── README.md

How the Program Works

The Tic-Tac-Toe board is represented using a list containing 9 elements:

board = [
    'X', ' ', ' ',
    ' ', 'O', ' ',
    ' ', ' ', 'X'
]


The positions correspond to the board as follows:

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8


For example, the initial sample state:

X |   |  
---------
  | O |  
---------
  |   | X

Players

The program defines two players:

AI = 'O'
HUMAN = 'X'

X represents the human player.
O represents the AI player.
Functions
print_board(board)

Displays the current Tic-Tac-Toe board in a readable 3×3 format.

Example:

X |   |  
---------
  | O |  
---------
  |   | X

check_winner(board)

Checks whether either player has won.

It evaluates:

3 rows
3 columns
2 diagonals

Possible return values are:

'X'       → Human wins
'O'       → AI wins
'Draw'    → Board is full with no winner
None      → Game is still in progress

available_moves(board)

Returns a list containing the indexes of all empty cells.

For example:

[1, 2, 3, 5, 6, 7]


means those positions are available for a move.

minimax(board, is_maximizing)

This is the main AI decision-making function.

The Minimax algorithm recursively explores possible future game states.

When the AI is playing:

AI → Maximizes the score


When the human is playing:

Human → Minimizes the score


The scoring system is:

+1 → AI wins
 0 → Draw
-1 → Human wins


The algorithm assumes that both players play optimally.

best_move(board)

Evaluates every available move for the AI and selects the move with the highest Minimax score.

It returns:

move_choice, best_score


where:

move_choice is the selected board position.
best_score is the evaluation of that move.
Minimax Strategy

The Minimax algorithm works by considering both the AI's moves and the human's possible responses.

The basic decision process is:

             AI Move
                |
       -------------------
       |        |        |
      Move 1   Move 2   Move 3
       |        |        |
   Human     Human     Human
   Moves     Moves     Moves
       |        |        |
     Score    Score    Score


The AI chooses the move with the maximum score, while assuming the human will choose moves that minimize the AI's score.

Sample Game State

The program starts with:

board = [
    'X', ' ', ' ',
    ' ', 'O', ' ',
    ' ', ' ', 'X'
]


The board is:

X |   |  
---------
  | O |  
---------
  |   | X


The program then calls:

move, score = best_move(board)


The AI evaluates all possible moves and selects the best one.

Running the Program

Save the Python code in a file named:

main.py


Run it using:

python main.py

Example Output
Initial Board:
X |   |  
---------
  | O |  
---------
  |   | X

AI (O) selects position: 1  | Evaluation score: 0

Board after AI move:
X | O |  
---------
  | O |  
---------
  |   | X


The exact selected position can depend on the order in which available moves are evaluated when multiple moves have the same Minimax score.

Evaluation Scores

The AI uses the following scoring system:

Result	Score
AI wins	1
Draw	0
Human wins	-1

Therefore, the AI attempts to maximize its score.

For example:

AI win   → +1
Draw     →  0
AI loss  → -1

Algorithm

The program follows these steps:

Display the current board.
Find all available positions.
Try each possible AI move.
Recursively simulate the human's responses.
Continue until the game reaches a win or draw.
Assign a score to the final state.
Select the move with the highest score.
Apply the selected move to the board.
Display the updated board.
Time and Space Complexity

For a standard Tic-Tac-Toe board, the total game tree is small enough for Minimax to examine completely.

In general, Minimax has approximately:

Time complexity: O(b^d)
Space complexity: O(d)

where:

b = branching factor (number of possible moves)
d = maximum depth of the game tree

Because Tic-Tac-Toe has only 9 cells, the algorithm is fast enough to run without optimization.

Advantages
Guarantees the optimal move when the complete game tree is searched.
Simple and effective for small games.
Does not require machine learning or training data.
Demonstrates fundamental game-playing AI concepts.
Limitations
The current program evaluates a single game state rather than running a complete interactive game.
Minimax can become computationally expensive for games with much larger game trees.
The implementation does not use optimizations such as alpha-beta pruning.
Possible Improvements

The project can be extended by:

Creating a complete human-vs-AI game.
Adding user input for moves.
Implementing alpha-beta pruning.
Adding difficulty levels.
Randomizing between equally good moves.
Adding a graphical user interface.
Keeping track of scores across multiple games.
Allowing the human to choose X or O.
Concepts Demonstrated

This project demonstrates several important Artificial Intelligence concepts:

Game-playing AI
Minimax search
Recursive algorithms
Decision making
State-space search
Utility/evaluation functions
Adversarial search
License

This project is provided for educational purposes and can be modified or extended for learning and experimentation.
