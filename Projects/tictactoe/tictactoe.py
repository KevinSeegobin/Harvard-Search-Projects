"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    xcount = 0
    ocount = 0
    for row in board:
        for column in row:
            if column == X:
                xcount += 1
            elif column == O:
                ocount +=1
    if xcount > ocount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()

    for row in range(3):
        for column in range(3):
            if board[row][column] == EMPTY:
                options.add((row, column))

    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] == EMPTY:
        new = copy.deepcopy(board) 
        new[action[0]][action[1]] = player(board)
        return new
    else:
        raise Exception("invalid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wincount = 0
    for row in range(3):
        if wincount == 3: break
        last = board[row][0]
        for column in range(3):
            if last == board[row][column] and last != None:
                wincount += 1
            else:
                wincount = 0
                break
    if wincount == 3: return last

    for column in range(3):
        if wincount == 3: break
        last = board[0][column]
        for row in range(3):
            if last == board[row][column] and last != None:
                wincount += 1
            else:
                wincount = 0
                break
    if wincount == 3: return last

    if board[1][1] != EMPTY:
        if board[0][0] == board[2][2] and board[1][1] == board[2][2]:
            return board[1][1]
        elif board[0][2] == board[2][0] and board[1][1] == board[0][2]:
            return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if any(EMPTY in row for row in board) and winner(board) == None:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    if terminal(board):
        return None
    if turn == X:
        optimum = maxplay(board)
    elif turn == O:
        optimum = minplay(board)
    return optimum[1]

def maxplay(board, v = [math.inf, None]):
    """
    returns the optimum move for max player(X)
    """
    if terminal(board):
        return [utility(board), None]
    
    options = actions(board)
    last = [-math.inf, None]
    
    for option in options:
        if last[0] <= v[0]:
            value = minplay(result(board, option), last)
            if last[0] < value[0]:
                value[1] = option
                last = value
        else:
            return [math.inf, None]

    return last

def minplay(board, v = [-math.inf, None]):
    """
    returns the optimum move for max player(X)
    """
    if terminal(board):
        return [utility(board), None]
    
    options = actions(board)
    last = [math.inf, None]
    
    for option in options:
        if last[0] >= v[0]:
            value = maxplay(result(board, option), last)
            if last[0] > value[0]:
                value[1] = option
                last = value
        else:
            return [-math.inf, None]

    return last