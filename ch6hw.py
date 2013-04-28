
#Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
# The program should work as follows.
#1. When the program begins, a random number in the range of 1 through 3 is generated.
#If the number is 1, then the computer has chosen rock. If the number is 2, then the computer has chosen paper.
# If the number is 3, then the computer has chosen scissors.
#(Don’t display the computer’s choice yet.)
#2. The user enters his or her choice of “rock”, “paper”, or “scissors” at the keyboard.
#3. The computer’s choice is displayed.
#4. A winner is selected according to the following rules:
#• If one player chooses rock and the other player chooses scissors, then rock wins. (The rock smashes the scissors.)
#• If one player chooses scissors and the other player chooses paper, then scissors wins. (Scissors cuts paper.)
#• If one player chooses paper and the other player chooses rock, then paper wins. (Paper wraps rock.)
#• If both players make the same choice, the game must be played again to determine the winner.


import random

# Introduction to the game. Give instructions.
def introduce_game():
    print('Rock. Paper. Scissors.' '\n' 'Enter 1 for Rock, 2 for Paper or 3 for Scissors.', '\n')
    enter_player_answer()

# Generate random integers.
def generate_random_int():
    return random.randrange(1,3)

# Function that gets player choice with validation loop.
def enter_player_answer():
    player = int(input('Enter your choice: '))
# Input validation loop.
    while player != 1 and player != 2 and player != 3:
        print('Invalid entry. Please try again.')
        player = int(input('Enter 1, 2, or 3.: '))
    display_computer_answer(player)

# Function that displays computer answer.
def display_computer_answer(player):
    c_answer = generate_random_int()
    print('Computer picks: ', c_answer, '\n')
    determine_winner(c_answer, player)

#Function that determines the winner.
def determine_winner(c, p):
    if c == p:
        print('Try again.')
        enter_player_answer()
    elif c == 1 and p == 2:
        print('Paper covers rock. Player wins!')
    elif c == 1 and p == 3:
        print('Rock smashes scissors. Computer Wins.')
    elif c == 2 and p == 1:
        print('Paper covers rock. Computer Wins.')
    elif c == 2 and p == 3:
        print('Scissors cut paper. Player wins!')
    elif c == 3 and p == 1:
        print('Rock smashes scissors. Player wins!')
    elif c == 3 and p == 2:
        print('Scissors cut paper. Computer wins!' )


introduce_game()

