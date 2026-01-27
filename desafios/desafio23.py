# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

#n = input('Insira um dígito de 0 a 9999 ')

#print(n[0])
#print(n[1])
#print(n[2])
#print(n[3])

n = int(input('Digite um numero '))
n1 = n//1000
n2 = (n//100)%10
n3 = ((n//10)%100)%10
n4 = ((n%1000)%100)%10

print(f'{n1}')
print(f'{n2}')
print(f'{n3}')
print(f'{n4}')
