n = int(input())
m = int(input())
'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def inverter(lista):
    inicio, fim = 0, len(lista) - 1
    
    while inicio > fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    return lista

print(inverter([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

vetor = []
for i in range(m):
    resposta = int(input())

    if resposta <= n:
        vetor.append(resposta)

for i in range(len(vetor)):
    for j in range(len(vetor)):
        if i < len(vetor) and j < len(vetor):
            if vetor[i] == vetor[j] and j != i:
                vetor.pop(j)
                j = j - 1
print(n - len(vetor))

