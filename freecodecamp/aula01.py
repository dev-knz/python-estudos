# Learn about variables and functions

import random

def get_choices():
    player_choice = input('Enter a choice (rock, paper or scissors): ')
    options = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(options)

    choice = {'player': player_choice, 'computer': computer_choice}

    return choice

def check_win(player, computer):
    print(f'You chose {player}\nComputer chose {computer}')
    if player == computer:
        return "It's a tie!" 
    if player == 'rock':
        if computer == 'paper':
            return 'Paper covers rock! You lose!'
        else:
            return 'Rock smashes scissors! You win!'
    if player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! You win!'
        else: 
            return 'Scissors cut paper! You lose' 
    if player == 'scissors':
        if computer == 'rock':
            return 'Rock smashes scissors! You lose!'
        else:
            return 'Scissors cut paper! You win!'
        
choices = get_choices()

result = check_win(choices["player"], choices["computer"])
print(result)

# 44:02 video 