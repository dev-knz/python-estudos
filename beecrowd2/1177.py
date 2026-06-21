from math import sqrt

def segundo_grau():
    print('ax² + bx + c')

    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    delta = n2**2 - (4 * n1 * n3)
    x1 = ((n2*-1) + sqrt(delta)) / 2 * n1
    x2 = ((n2*-1) - sqrt(delta)) / 2 * n1
    return x1, x2

print(segundo_grau())

