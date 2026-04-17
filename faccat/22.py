x = int(input())

y = int(input())

def cinema(a):
    if a <= 17:
        soma = 15
    
    elif 18 <= a <= 59:
        soma = 30

    else:
        soma = 20
    return soma

print(cinema(x) + cinema(y))