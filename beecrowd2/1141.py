def Le_Lista():
    lista = []
    
    entrada = input().split()
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista
    
def Calcula_Faces(lista):
    faces = []
    
    for i in range(1, 7):
        qntd = 0
        for j in range(len(lista)):
            if i == lista[j]:
                qntd += 1
        faces.append(qntd)
    return faces
    
def Calcula_Maior(lista):
    for i in range(len(lista)):
        if i == 0:
            maior = lista[i]
            dado = i
        else:
            if lista[i] > maior:
                maior = lista[i]
                dado = i
    dado += 1
    return f'A face {dado} tem o maior número de ocorrências: {maior}'

def Imprime_lista(lista):
    for i in range(len(lista)):
        print(f'Número de ocorrências da face {i+1} = {lista[i]}')

lst = Le_Lista()
faces = Calcula_Faces(lst)
Imprime_lista(faces)
print(Calcula_Maior(faces))