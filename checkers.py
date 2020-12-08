'''
== Board Positions ==

 1 . 2 . 3 . 4 .
 . 5 . 6 . 7 . 8
10 .11 .12 .13 .
 .14 .15 .16 .17
19 .20 .21 .22 .
 .23 .24 .25 .26
28 .29 .30 .31 .
 .32 .33 .34 .35

== Board State Representation
 - Dictionary with keys 'x', 'o', '-'
 - Values are a list of the positions taken by each type of piece


== Moves ==
 - Moves are lists of tuples (lists because a move can have several sub-moves)
 - Each tuple will be in the form (position of the piece to move, position to move the piece to)

'''

def initial_game():
    state = {}
    state['x'] = [x for x in range(1,14) if x%9 != 0]
    state['-'] = [x for x in range(14,23) if x%9 != 0]
    state['o'] = [x for x in range(23,36) if x%9 != 0]
    return state

def game_over(state):
    for piece, taken_positions in state.items():
        if (piece in ['o', 'x']) and (len(taken_positions) == 0):
            return True
    return False

def winner(state):
    if not game_over(state):
        print('Game not over')
    else:
        for piece, taken_positions in state.items():
            if (piece in ['o', 'x']) and (len(taken_positions) != 0):
                return piece

def computer_play(state, piece):
    return move

def update_board(state, move, piece):
    return state


# starting game
state = initial_game()
print(state)
while not game_over(state):

    #play computer - ninitially computer will be x piece
    computer_play(state, 'x')
    if game_over(state):
        break

    #play player



print(f'The winner is {winner(state)}')