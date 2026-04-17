number = [10, 21, 4, 45, 66, 93, 11]

par, impar = 0, 0

for i in number:
    if i % 2 == 0:
        par += 1
    
    else:
        impar += 1

print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')