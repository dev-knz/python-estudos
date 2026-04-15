votos = int(input())

brancos = int(input('Votos em branco: '))
validos = int(input('Votos válidos: '))

nulo = votos - (validos + brancos)

print(f'Eleição 2026:\nVotos válidos: {validos/votos * 100:.0f}%\nBrancos: {brancos/votos * 100:.0f}%\nNulo: {nulo/votos * 100:.0f}%')