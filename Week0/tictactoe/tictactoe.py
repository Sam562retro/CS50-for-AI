"""
Tic Tac Toe Player
"""

# Note: The X player will always start first and is player 1.

import copy

X = "X"
O = "O"
EMPTY = None
INFINITY = 1e3


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xs = 0
    os = 0
    for row in board:
        for cell in row:
            if cell == 'X':
                xs+=1
            elif cell == 'O':
                os+=1
            else:
                pass
    if xs == os:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j] == EMPTY):
                possible.add((i, j))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible = actions(board)
    if action not in possible:
        raise Exception

    new = copy.deepcopy(board)
    new[action[0]][action[1]] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    00 10 20
    01 11 21
    02 12 22

    00 01 02
    10 11 12
    20 21 22

    00 11 22
    02 11 20
    """
    possible = actions(board)
    if(board[0][0] == board[1][0] == board[2][0] != EMPTY):
        return board[0][0]
    elif(board[0][1] == board[1][1] == board[2][1] != EMPTY):
        return board[0][1]
    elif(board[0][2] == board[1][2] == board[2][2] != EMPTY):
        return board[0][2]
    elif(board[0][0] == board[0][1] == board[0][2] != EMPTY):
        return board[0][1]
    elif(board[1][0] == board[1][1] == board[1][2] != EMPTY):
        return board[1][1]
    elif(board[2][0] == board[2][1] == board[2][2] != EMPTY):
        return board[2][1]
    elif(board[0][0] == board[1][1] == board[2][2] != EMPTY):
        return board[0][0]
    elif(board[0][2] == board[1][1] == board[2][0] != EMPTY):
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    a = winner(board)
    if a == "X":
        return 1
    elif a == "O":
        return -1
    else:
        return 0


def mini(board):
    v = INFINITY

    if terminal(board):
        return utility(board)

    for a in actions(board):
        v = min(v, maxi(result(board, a)))
    return v

def maxi(board):
    v = -INFINITY

    if terminal(board):
        return utility(board)

    for a in actions(board):
        v = max(v, mini(result(board, a)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if not terminal(board):
        m = player(board)
        if m == "X":
            v = -INFINITY
            for a in actions(board):
                o = mini(result(board, a))
                if o > v:
                    v = o
                    act = a
        else:
            v = INFINITY
            for a in actions(board):
                o = maxi(result(board, a))
                if o < v:
                    v = o
                    act = a

        return act
    else:
        return None
