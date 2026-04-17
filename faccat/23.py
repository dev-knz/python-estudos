
vitorias, derrotas = 0, 0

for i in range(6):
    n = str(input()).upper()

    if n == 'V':
        vitorias += 1

    else:
        derrotas += 1

if not vitorias:
    print('-1')
elif 1 <= vitorias <= 2:
    print('3')
elif 3 <= vitorias <= 4:
    print('2')
else:
    print('1')