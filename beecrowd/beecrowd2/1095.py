# Variáveis e Inputs
x1, y1 = input().split()
x2, y2 = input().split()

# Conversão
x1 = int(x1)
y1 = int(y1)

x2 = int(x2)
y2 = int(y2)

# Ver quem é o maior, pra evitar erros de lógica dentro do programa.
if y1 > y2:
    y1, y2 = y2, y1

if x1 > x2:
    x1, x2 = x2, x1

# Pegando uma variável responsável pela definição do tamanho do for
num = int(input())

# Definindo uma variável para a contagem das árvores dentro da área
contador = 0

for i in range(num):
    x, y = input().split()
    
    x = int(x)
    y = int(y)
    
    if x1 <= x <= x2 and y1 <= y <= y2:
        contador += 1
        
print(contador)
