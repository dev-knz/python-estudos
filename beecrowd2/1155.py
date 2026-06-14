def Imprime_Fibonacci(num):
    f1 = 1
    f2 = 1
    
    for i in range(num):
        if i <= 1:
            print(f'1', end=' ')
        else:
            f3 = f1 + f2
            print(f3, end=' ')
            f1, f2 = f2, f3
    
n = int(input())
Imprime_Fibonacci(n)