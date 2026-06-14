def Le_movimento():
    direcao, distancia = input().split()

    direcao = int(direcao)
    distancia = int(distancia)
    return direcao, distancia

def Atualiza_posicao(x, y, dir, dist):
    if dir == 1:
        y = y + dist
    elif dir == 2:
        x = x - dist
    elif dir == 3:
        y = y - dist
    else:
        x = x + dist
    return x, y

def Verifica_posicao(x, y, d):
    from math import sqrt
    distancia = sqrt(x**2 + y**2)

    if distancia > d:
        return False
    else:
        return True

posicao = [0,0]

n, d = input().split()

n = int(n)
d = int(d)

i = 0
while i < n:
    variavel = Le_movimento()
    atualiza = Atualiza_posicao(posicao[0], posicao[1], variavel[0], variavel[1])
    posicao[0], posicao[1] = atualiza[0], atualiza[1]
    resposta = Verifica_posicao(posicao[0], posicao[1], d)

    if not resposta:
        print('S')
        break
    i += 1
if resposta:
    print('N')

    
