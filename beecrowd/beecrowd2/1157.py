n = str(input())
dna = str(input())
resposta = ''
contagem = 0

i = 0
inicio, fim = 0, len(n) - 1

while fim <= len(dna) - 1:
    if i <= fim:
        resposta += dna[i]
    if i == fim:

        if resposta == n:
            contagem += 1
        resposta = ''
        inicio += 1
        i = inicio - 1
        fim += 1
    i += 1
    
print(contagem)