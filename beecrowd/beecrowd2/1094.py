# Variável para a senha
num = int(input())

# Variável que vai somar os dígitos
soma = 0

while num != 0:
    ultimo = num % 10
    num = num // 10
    
    soma += ultimo
print(soma)
    
    