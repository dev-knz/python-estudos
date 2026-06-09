def Busca_String(string1, string2):
    contagem = 0
    aux = 0
    for i in range(len(string1)):
        if string1[i] in string2:
            aux += 1
        else:
            aux = 0

        if aux == len(string2):
            aux = 1
            contagem += 1

    
    return contagem

texto1 = input().lower()
texto2 = input().lower()

print(Busca_String(texto1, texto2))