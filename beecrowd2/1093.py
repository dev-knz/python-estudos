# Capacidade total do reservatório
c = int(input())

# Litros adicionados pela bomba durante o dia
b = int(input())

# Litros perdidos pelo vazamento durante a noite
v = int(input())

# Criando a variável para armazenar os dias!
dia = 0

# Saldo
saldo = 0
while saldo < c:
    saldo += b
    
    if saldo >= c:
        dia += 1
    
    else:
        saldo -= v
        dia += 1
    
print(dia)

