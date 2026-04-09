num = int(input())
qtnd = 0

while num > 0:
    # Tirar dígito
    num = num // 10
    qtnd += 1

print(qtnd)