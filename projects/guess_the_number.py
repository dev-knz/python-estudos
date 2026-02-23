import random

computer_choice = random.randint(1,100)
attempts = 0

while True:
    player_choice = int(input('Choice a number (1-100): '))
    attempts += 1

    result = abs(computer_choice - player_choice)
    if result == 0:
        print(f'You guessed in {attempts} attempts!')
        break
    elif result < 6 and result > 0:
        print(f'Very close!')
    elif result > 5 and result < 16:
        print(f'Close!')
    elif result > 15 and result < 31:
        print(f'Not too far...')
    else:
        print(f'Far away!')