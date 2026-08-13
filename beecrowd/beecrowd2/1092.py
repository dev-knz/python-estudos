
n1 = int(input())
n2 = int(input())
n3 = int(input())

# Verificando para cada caso a temperatura média entre extremos
if n1 >= n2 and n2 >= n3:
    temperatura = n2

elif n3 >= n2 and n2 >= n1:
    temperatura = n2
    
elif n2 >= n1 and n1 >= n3:
    temperatura = n1

elif n3 >= n1 and n1 >= n2:
    temperatura = n1

elif n2 >= n3 and n3 >= n1:
    temperatura = n3

else:
    temperatura = n3
    
print(temperatura)