def decrescente(a, b, c):
    if a > b and a > c:
        if b > c:
            return a,b,c
        return a,c,b

    elif b > a and b > c:
        if a > c:
            return b,a,c
        return b,c,a

    else:
        if a > b:
            return c, a, b
        return c,b,a

n1, n2, n3 = map(int, input().split())
print(decrescente(n1,n2,n3))