number = [5, 20, 15, 20, 25, 50, 20]

alvo = int(input())

for i in number:
    if i == alvo:
        number.remove(alvo)
print(number)