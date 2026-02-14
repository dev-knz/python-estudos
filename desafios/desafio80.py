# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())

lista = []
h = cont = 0
for i in range(0, 5):
    n = int(input('Insira um valor: '))

    if i == 0:
        lista.append(n)
    else: 
        cont = 0
        for h in range(0, len(lista)):
            if n < lista[h]:
                lista.insert(h, n)
                break
            
            cont += 1
            if cont == len(lista):
                lista.append(n)
                break
            
        
print(lista)
            
            