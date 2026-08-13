n = int(input())

tabuleiro = []
for i in range(n):
    tabuleiro.append(int(input()))
    
for i in range(n):
    bombas = 0
    
    if i == 0:
        bombas = tabuleiro[i] + tabuleiro[i+1]
    elif i == (n-1):
        bombas = tabuleiro[i-1] + tabuleiro[i]
    else:
        bombas = tabuleiro[i-1] + tabuleiro[i] + tabuleiro[i+1]
        
    print(bombas)
    
        