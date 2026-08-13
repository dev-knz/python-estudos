def Le_Lista():
    lista = []

    entrada = input().split()
    for i in range(len(entrada)):
        lista.append(int(entrada[i]))
    return lista

def Remove_Iguais(l1, l2):
    i = 0
    while i < len(l1):
        trocar = False
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                trocar = True
        if trocar:
            for k in range(i, len(l1) - 1):
                l1[k] = l1[k+1]
            l1.pop()
        else:
            i = i + 1
    return l1

l1 = Le_Lista()
l2 = Le_Lista()

Remove_Iguais(l1, l2)
print(l1)