import random

words = ['python', 'world', 'minecraft', 'planet']
words = random.choice(words)
letters = list()

for l in words:
    letters.append('_')

corrects = errors = 0
while True:
    temp = 0
    if corrects == len(letters):
        print('You Win!')
        break
    elif errors == 6:
        print('You Lose!')
        break

    print(" ".join(letters))
    attempt = str(input())

    for c, v in enumerate(words):
        if attempt == v:
            letters[c] = attempt
            corrects += 1
            temp += 1
    
    if temp == 0:
        errors += 1

print(f"The word is {words} ")


