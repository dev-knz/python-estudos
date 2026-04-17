tamanho = int(input())
quadrado, n = "", 1

for i in range(tamanho):
    if quadrado != "":
        quadrado += "\n"

    if i % 2 != 0:
        n += tamanho - 1
        for j in range(tamanho):
            quadrado += str(n) + " "
            n -= 1

    else:
        if quadrado != "":
            n += tamanho + 1

        for j in range(tamanho):
            quadrado += str(n) + " "
            n += 1

print(quadrado)