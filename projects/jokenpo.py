# Jokenpo melhor de 3 pontos.
import random

def check_win(player, computer):
    print(f'Player choice: {player} | Computer choice: {computer}')

    if player == computer:
        print("It's a draw!")
    elif player == 'rock':
        if computer == 'paper':
            print('Paper covers rock! You lose!')
            win_computer = 'Computer Win'
            return win_computer
        else:
            print('Rock smashes scissors! You win')
            win_player = 'Player Win'
            return win_player
    elif player == 'paper':
        if computer == 'rock':
            print('Paper covers rock! You win!')
            win_player = 'Player Win'
            return win_player
        else:
            print('Scissors cut paper! You lose!')
            win_computer = 'Computer Win'
            return win_computer
    elif player == 'scissors':
        if computer == 'paper':
            print('Scissors cut paper! You win!')
            win_player = 'Player Win'
            return win_player
        else:
            print('Rock smashes scissors! You lose!')
            win_computer = 'Computer Win'
            return win_computer

player = computer = 0
option = ['rock', 'paper', 'scissors']

while True:
    if player == 3:
        print('The player win 3 times!')
        break
    elif computer == 3:
        print('The computer win 3 times!')
        break

    player_choice = input('Rock, paper or Scissors: ').lower()
    computer_choice = random.choice(option)

    
    if player_choice in option:
           result = check_win(player_choice, computer_choice)
           if result == 'Computer Win':
               computer += 1
               print(f'Computer has {computer} point(s)')

           if result == 'Player Win':
               player += 1
               print(f'Player has {player} point(s)')
    else:
        print('ValueERROR in the choice of options.')



    
