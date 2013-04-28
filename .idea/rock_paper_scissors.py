from random import randint




def make_selection():
    possibilities = ['rock', 'paper', 'scissors']
    # Return a random element from the list of possibilities
    return possibilities[randint(0, len(possibilities) - 1)]



