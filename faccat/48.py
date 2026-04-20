
number = [10, 20, 30, 40, 50]

contexto = int(input())
novo = int(input())

for i in range(len(number)):
    if number[i] == contexto:
        number.insert(i, novo)
        break

print(number)