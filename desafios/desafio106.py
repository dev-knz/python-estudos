# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM' o programa se encerrará.

while True:
    n = str(input('Insira o comando a ser pesquisado no help(): '))

    if n == 'FIM':
        break

    else:
        print(help(n))
